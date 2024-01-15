from abc import ABC, abstractmethod
import random
from board import Direction


class Strategy(ABC):
    def __init__(self, ghost):
        self._ghost = ghost
    
    def _distances(self, position:tuple, speed, num = 2):
        moves = self._ghost.get_board().possible_moves(self._ghost.rect.center, speed, self._ghost.direction, num)       
        tile_width, tile_height = self._ghost.get_board().tile_dimension()
        
        distance = [None, None, None, None]

        board = self._ghost.get_board()

        def tup_add(tup1, tup2):
            return (tup1[0]+tup2[0], tup1[1]+tup2[1])
        gh_pos = self._ghost.get_position()

        if moves[int(Direction.LEFT)]:
            distance[int(Direction.LEFT)] = board.manhatan_distance(tup_add(gh_pos, (-tile_width, 0)), position)

        if moves[int(Direction.RIGHT)]:
            distance[int(Direction.RIGHT)] = board.manhatan_distance(tup_add(gh_pos, (tile_width, 0)), position)
        
        if moves[int(Direction.UP)]:
            distance[int(Direction.UP)] = board.manhatan_distance(tup_add(gh_pos, (0, -tile_height)), position)
        
        if moves[int(Direction.DOWN)]:
            distance[int(Direction.DOWN)] = board.manhatan_distance(tup_add(gh_pos, (0, tile_height)), position)

        return distance

    def _next_move_min(self, position:tuple, num =2) -> Direction:
        distance = self._distances(position,self._ghost.speed, num)
        min_distance = min([x for x in distance if x is not None])
        return Direction(distance.index(min_distance))

    @abstractmethod
    def make_a_move(self):
        pass


class InCage(Strategy):
    def __init__(self, ghost):
        super().__init__(ghost)
        self.__prev_direction = self._ghost.direction

    
    def make_a_move(self):
        moves = self._ghost.get_board().possible_moves(self._ghost.rect.center, self._ghost.speed, self._ghost.direction)
        
        if moves[int(self.__prev_direction)]:
            self._ghost.simple_move(self.__prev_direction)
        elif moves[int(self.__prev_direction.inverse())]:
            self._ghost.simple_move(self.__prev_direction.inverse())
            self.__prev_direction = self.__prev_direction.inverse()




class Walk(Strategy):
    def __init__(self, ghost):
        super().__init__(ghost)
        self.__i = 0
        
        self._inv_move = [False, False, False, False]

    # Make a random move, i goes for the index, so that if a ghost picks direction
    # We keep the revese move so a ghost does not oscillate
    def make_a_move(self):
        tile_width, tile_height = self._ghost.get_board().tile_dimension()
        moves = self._ghost.get_board().possible_moves(self._ghost.rect.center, self._ghost.speed, self._ghost.direction)
        if self.__i == 0 or not moves[int(self._ghost.direction)]:
            to_choose = [i for i in range(len(moves)) if (moves[i] and not self._inv_move[i])]
            if to_choose:
                self._ghost.direction = Direction(random.choice(to_choose))
            self.__i = 0
        self.__i += 1

        if self.__i > tile_width//self._ghost.speed:
            self.__i = 0

        self._inv_move = [False, False, False, False]        

        self._ghost.simple_move(self._ghost.direction)
        self._inv_move[int(self._ghost.direction.inverse())] = True


class GoTo(Strategy):
    def __init__(self, ghost):
        super().__init__(ghost)
        self.__i = 0
        self.__turning = False

        
    @abstractmethod
    def make_a_move(self):
        pass
    
    # check if the ghost got into the vicinty of the given tile
    def _check_if_got_to(self, x_tile, y_tile):  
        tile_width, tile_height = self._ghost.get_board().tile_dimension()
        
        if ( x_tile -1 <= self._ghost.get_position()[0]/tile_width <= x_tile + 1) and \
              ( y_tile - 1 < self._ghost.get_position()[1]/tile_height < y_tile+1):
                return True
                
        return False

    # idea: move to the tile that minimizes the direction
    # problem: 2 tiles may 2 equally distant
    # then prefer the turning over going backwards
    def get_to_the(self, x_tile, y_tile, num = 2) -> bool:
        if self._check_if_got_to(x_tile, y_tile): return True
        tile_width, tile_height = self._ghost.get_board().tile_dimension()

        moves = self._ghost.get_board().possible_moves(self._ghost.rect.center, self._ghost.speed, self._ghost.direction)            
        if self.__turning:
            direction = self._ghost.direction
            self.__i += 1
            if not moves[int(direction)]:
                self.__turning = False
                self.__i = 0
                direction = self._next_move_min((x_tile*tile_width, y_tile*tile_height), num)

        
        if self.__i > tile_height//self._ghost.speed:
            self.__i = 0
            self.__turning = False


        if not self.__turning:
            direction = self._next_move_min((x_tile*tile_width, y_tile*tile_height), num)            
            can_turn = [moves[j] if j not in (int(self._ghost.direction), int(self._ghost.direction.inverse())) else False for j in range(len(moves))]

            if (True in can_turn):
                dist = self._distances((x_tile*tile_width, y_tile*tile_height), self._ghost.speed, num=3)
                min_dist_to_turn = min([dist[i] for i in range(len(moves)) if can_turn[i]])  
                current_dist = self._ghost.get_board().manhatan_distance(self._ghost.get_position(), (x_tile*tile_width, y_tile*tile_height))
                
                if min_dist_to_turn < current_dist or not moves[int(self._ghost.direction)]:  
                    self.__turning = True
                    self.__i = 0
                    dist = [dist[i] if can_turn[i] else None for i in range(len(dist))]
                    direction = Direction(dist.index(min_dist_to_turn))
   


        if moves[int(self._ghost.direction)] and direction == self._ghost.direction.inverse():
            direction = self._ghost.direction

        self._ghost.simple_move(direction)
        
        return False

#Strategy to get out of the cage     
class GetOut(GoTo):   
    def __init__(self, ghost):
        super().__init__(ghost)
        self._ghost.getting_out = True


    def make_a_move(self):
        i,j = self._ghost.get_board().get_out_position()
        got_to = self.get_to_the(i,j)
        if got_to:
            self._ghost.set_strategy(Walk(self._ghost))
            self._ghost.getting_out = False      

    # We overwrite the go_to_the method since the base class method doesn't really pass here
    # because the cage is special and turning whenever possible is just a bad idea
    def get_to_the(self, x_tile, y_tile) -> bool:
        if self._check_if_got_to(x_tile, y_tile): return True

        tile_width, tile_height = self._ghost.get_board().tile_dimension()
        moves = self._ghost.get_board().possible_moves(self._ghost.rect.center, self._ghost.speed, self._ghost.direction)            
        
        direction = self._next_move_min((x_tile*tile_width, y_tile*tile_height), 3)
        if int(direction) == int(self._ghost.direction.inverse()) and moves[int(self._ghost.direction)]:
            direction = self._ghost.direction

        self._ghost.simple_move(direction)
        
        return False
    
# Follow 
class Follow(GoTo):
    def __init__(self, ghost, pacman):
        super().__init__(ghost)
        self.__pacman = pacman

    def make_a_move(self):
        tile_width, tile_height = self._ghost.get_board().tile_dimension()
        i,j = self.__pacman.get_position()[0]/tile_width, self.__pacman.get_position()[1]/tile_height
        self.get_to_the(i,j)



class Frightened(Strategy):
    def __init__(self, ghost, pacman):
        super().__init__(ghost)
        self.__pacman = pacman
        self._scared_speed = 1
        self.__walk_strategy = Walk(self._ghost)
        self.__incage_strategy = InCage(self._ghost)
        self.__i = 0
        self.__prev_direction = self._ghost.direction
    
    # Idea:
    # If a ghost gets in the vicinity of pacman, then it tries to run away
    # otherwise it moves randomly 
    # also we account here that in the moment of activation the ghost could be getting out
    # or was doing incage movement
    def make_a_move(self):
        if not self._ghost.inCage and not self._ghost.getting_out:     
            tile_width, tile_height = self._ghost.get_board().tile_dimension()
            treshhold = (7 * tile_width)**2

            ghost_pacman_distance = (self._ghost.get_position()[0] - self.__pacman.get_position()[0])**2 + (self._ghost.get_position()[1] - self.__pacman.get_position()[1])**2
            
            if ghost_pacman_distance<treshhold:
                moves = self._ghost.get_board().possible_moves(self._ghost.rect.center, self._ghost.speed, self.__prev_direction)
                if self.__i < tile_width and moves[int(self.__prev_direction)]:
                    self._ghost.simple_move(self.__prev_direction)
                    self.__i += 1 
                else:
                    distances = self._distances(self.__pacman.rect.center,self._scared_speed)                
                    max_distance = max([x for x in distances if x is not None])
                    direction = Direction(distances.index(max_distance))         
                    self._ghost.simple_move(direction)
                    self.__prev_direction = direction
                    self.__i = 0

            else: 
                self.__walk_strategy.make_a_move()
        
        elif self._ghost.inCage:
            self.__incage_strategy.make_a_move()
        elif self._ghost.getting_out:
            GetOut(self._ghost).make_a_move()
            

class Eaten(GoTo):   
    def __init__(self, ghost):
        super().__init__(ghost)
        self._ghost.ressurectred = True
        self._ghost.frightened = False
        
    # the position inside the gates
    def make_a_move(self):
        i,j = self._ghost.get_board().get_eyes_back_position()
        got_to = self.get_to_the(i,j, num = 3)
        if got_to:
            self._ghost.got_to_cage = True


        
    
        

        




    


