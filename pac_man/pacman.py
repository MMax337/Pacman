import pygame
from board import Board, Direction
from keyboard_manager import KeyManager
import os

pygame.init()
class PacMan(pygame.sprite.Sprite):
    def __init__(self, board: Board, key_manger: KeyManager, score:int = 0, lives:int=3) -> None:
        super().__init__()
        self.__board = board
        size = (self.__board.tile_dimension()[0]+10,self.__board.tile_dimension()[0]+10)
        self.__pac_man_hello = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','pac_man','hello_pacman.png')).convert_alpha(),size)
        self.__pac_man_left  = [
                                pygame.transform.smoothscale(pygame.image.load(os.path.join('images','pac_man','pac_man_left_1.png')).convert_alpha(), size),
                                pygame.transform.smoothscale(pygame.image.load(os.path.join('images','pac_man','pac_man_left_2.png')).convert_alpha(), size)
                               ]
        
        self.__pac_man_right = [
                                pygame.transform.smoothscale(pygame.image.load(os.path.join('images','pac_man','pac_man_right_1.png')).convert_alpha(), size),
                                pygame.transform.smoothscale(pygame.image.load(os.path.join('images','pac_man','pac_man_right_2.png')).convert_alpha(), size)
                               ]
    
        self.__pac_man_up  =   [pygame.transform.rotate(self.__pac_man_right[0], 90), pygame.transform.rotate(self.__pac_man_right[1], 90)]
        self.__pac_man_down  = [pygame.transform.rotate(self.__pac_man_left[0], 90), pygame.transform.rotate(self.__pac_man_left[1], 90)]
        
        self.__pac_man_death = [
            pygame.transform.rotate(
                    pygame.transform.smoothscale(
                        pygame.image.load(os.path.join('images','pac_man','death',f'pacman_death-{i}.png')).convert_alpha(), size),90) 
            for i in range(46)]
    


        self.image = self.__pac_man_hello
        self.rect = self.image.get_rect(center = self.__board.pac_man_start_position()) 
        self.__key_manager = key_manger
        self.__score = score
        self.__lives = lives
        self.__animation_index = 0
        self.__speed = 5
        self.__current_direction = Direction.LEFT
        self.__next_direction = Direction.LEFT
        self.__dead = False
        self.__powerup_activated = False
        self.__death_animation = 0
    

    @property
    def dead(self):
        return self.__dead
    
    @dead.setter
    def dead(self, state: bool):
        self.__dead = state

    def lives(self):
        return self.__lives
    
    def life_decrease(self):
        self.__lives-=1

    def get_score(self):
        return self.__score 

    def is_powerup_activated(self):
        return self.__powerup_activated
    
    def disable_powerup(self):
        self.__powerup_activated = False
    
    def get_position(self):
        return self.rect.center
    
    def update(self):
        if not self.dead:
            self.rect.centerx,self.rect.centery = self.__board.tunneling(self.rect.center)
            self.__move()
        else:
            # play death animation:
            if self.__death_animation < len(self.__pac_man_death):
                self.image = self.__pac_man_death[int(self.__death_animation)]
                self.__death_animation +=0.25
            else:
                self.__lives -= 1
                if self.__lives > 0:
                    self.dead = False
                    self.rect.centerx, self.rect.centery = self.__board.pac_man_start_position()
                    self.image = self.__pac_man_hello
                    self.__current_direction = Direction.LEFT
                    self.__next_direction = Direction.LEFT
                    self.__death_animation = 0
                else:
                    self.image = self.__pac_man_death[45]

    # Method for start animation
    def start(self):
        self.__direction_change()
        self.__arrow_draw()
    
    def __direction_change(self):
        direction = self.__key_manager.get_direction()
        if direction is not None:
            self.__next_direction = direction
    
    def __move(self):
        self.__direction_change()
        moves = self.__board.possible_moves(self.rect.center, self.__speed, self.__current_direction)
        self.__animation_index += 0.125 # 0.125 is 2^(-3) => accuracy  
     

        #Try to move to the next direction:
        if moves[int(self.__next_direction)]: self.__current_direction = self.__next_direction

        
        if self.__animation_index >= len(self.__pac_man_left): self.__animation_index = 0
        
        if moves[int(self.__current_direction)]:
            if self.__current_direction == Direction.LEFT:
                self.rect.centerx -= self.__speed 
                self.image = self.__pac_man_left[int(self.__animation_index)]
            
            elif self.__current_direction == Direction.RIGHT:
                self.rect.centerx += self.__speed 
                self.image = self.__pac_man_right[int(self.__animation_index)]
            
            elif self.__current_direction == Direction.UP:
                self.rect.centery -= self.__speed 
                self.image = self.__pac_man_up[int(self.__animation_index)]
            
            elif self.__current_direction == Direction.DOWN:
                self.rect.centery += self.__speed 
                self.image = self.__pac_man_down[int(self.__animation_index)]
            
        self.__arrow_draw()
        self.__eat()

    def __arrow_draw(self):
        offset = 25
        arrow_width = self.rect.width//3
        x,y = self.rect.center
        if self.__next_direction == Direction.LEFT:
            pygame.draw.polygon(self.__board.get_screen(), 'yellow', ([(x-offset, y-arrow_width//2), (x-offset, y+arrow_width//2), (x-1.5*offset, y)]))
        elif self.__next_direction == Direction.RIGHT:
            pygame.draw.polygon(self.__board.get_screen(), 'yellow', ([(x+offset, y-arrow_width//2), (x+offset, y+arrow_width//2), (x+1.5*offset, y)]))
        elif self.__next_direction == Direction.UP:
            pygame.draw.polygon(self.__board.get_screen(), 'yellow', ([(x-arrow_width//2, y-offset), (x+arrow_width//2, y-offset), (x, y-1.5*offset)]))
        elif self.__next_direction == Direction.DOWN:
            pygame.draw.polygon(self.__board.get_screen(), 'yellow', ([(x-arrow_width//2, y+offset), (x+arrow_width//2, y+offset), (x, y+1.5*offset)]))
    
    #Interact with the board
    def __eat(self):
        tile_width, tile_height = self.__board.tile_dimension()
        # i,j are tile position
        i,j = self.rect.centery//tile_height, self.rect.centerx//tile_width
        
        # Here no offset needed since we look at the rect.center and pacman radius
        # is about 1/2 the tile width
        val = self.__board.get_value(i,j)
        if val == 1:
            self.__board.erase_value(i,j)
            self.__score += 10
        if val == 2:
            self.__board.erase_value(i,j)
            self.__powerup_activated = True
            self.__score += 50




    
    
        
