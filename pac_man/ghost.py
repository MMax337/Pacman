import pygame
import os
from board import Board, Direction
from strategy import InCage, Walk, Frightened, Eaten
from abc import ABC, abstractmethod


# Interface
class IGhost(pygame.sprite.Sprite,ABC):
    def __init__(self, board :Board) -> None:
        super().__init__()
        self._board = board
        self.speed = None
        self._strategy = None
        self.image = None
        self.rect = None
        self.direction = Direction.UP

    def get_board(self):
        return self._board
    
    def set_strategy(self, strategy):
        self._strategy = strategy

    @abstractmethod
    def simple_move(self, direction: Direction):
        pass
    
    def get_position(self):
        return self.rect.center

    def simple_move(self, direction: Direction):
        if direction == Direction.LEFT:
            self.rect.centerx -= self.speed   

        elif direction == Direction.RIGHT:
            self.rect.centerx += self.speed 

        elif direction == Direction.UP:
            self.rect.centery -= self.speed

        elif direction == Direction.DOWN:
            self.rect.centery += self.speed
        
        self.direction = direction
    
    def update(self) -> None:
        self.rect.centerx,self.rect.centery = self._board.tunneling(self.rect.center)
        self._strategy.make_a_move()
        



class Ghost(IGhost):
    def __init__(self, start_position, board :Board, inCage: bool, ghost_num, gettiing_out = False) -> None:
        super().__init__(board)

        size = (self.get_board().tile_dimension()[0]+20,self.get_board().tile_dimension()[0]+20)
        self.ghost_up = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','spirites',f'spirit{ghost_num}_up.png')).convert_alpha(),size)
        self.ghost_down = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','spirites',f'spirit{ghost_num}_down.png')).convert_alpha(),size)
        self.ghost_left = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','spirites',f'spirit{ghost_num}_left.png')).convert_alpha(),size)
        self.ghost_right = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','spirites',f'spirit{ghost_num}_right.png')).convert_alpha(),size)
        self.image = self.ghost_up
        
        self.getting_out = gettiing_out
        self.ghost_num = ghost_num
        self.rect = self.image.get_rect(center = start_position)
        self.inCage = inCage
        self.ressurectred = False
        self.speed = 3
        self.following = False
        self.direction = Direction.UP
        self._strategy = InCage(self) if inCage  else Walk(self)
    

    def set_speed(self, speed):
        self.speed = speed
        
    def simple_move(self, direction: Direction):
        if direction == Direction.LEFT:
            self.rect.centerx -= self.speed   
            self.image = self.ghost_left

        if direction == Direction.RIGHT:
            self.rect.centerx += self.speed  
            self.image = self.ghost_right

        if direction == Direction.UP:
            self.rect.centery -= self.speed 
            self.image =  self.ghost_up

        if direction == Direction.DOWN:
            self.rect.centery += self.speed 
            self.image = self.ghost_down
        
        self.direction = direction

        
class Scared_Ghost(IGhost):
    def __init__(self, start_position, board :Board, inCage: bool, getting_out,ghost_num, pacman) -> None:
        super().__init__(board)

        size = (self.get_board().tile_dimension()[0]+20,self.get_board().tile_dimension()[0]+20)
        self.__scared = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','spirites','scared.png')).convert_alpha(),size)
        self.__white_scared = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','spirites','white_scared.png')).convert_alpha(),size)
        self.image = self.__scared
        self.rect = self.image.get_rect(center = start_position)

        self.getting_out = getting_out
        self.ghost_num = ghost_num
        self.inCage = inCage
        self.speed = 1
        self._strategy = Frightened(self,pacman)
        self.direction = Direction.UP
        self.__blink = False
        self.__blinking_index = 0
    
    def update(self) -> None:
        if self.__blink:
            self.__blinking_index +=1
            if self.__blinking_index > 20: self.__blinking_index = 0
            if self.__blinking_index < 10:
                self.image = self.__white_scared
            else:
                self.image =self.__scared
        
        self.rect.centerx,self.rect.centery = self._board.tunneling(self.rect.center)
    
        self._strategy.make_a_move()
    
    # Blink to indicate the ending state of being scared
    def blinking(self, to_blink: bool):
        self.__blink = to_blink
        self.image = self.__white_scared if to_blink else self.__scared
    


    
        

class Eyes(IGhost):
    
    def __init__(self, start_position, board :Board, ghost_num) -> None:
        super().__init__(board)

        size = (self.get_board().tile_dimension()[0]+20,self.get_board().tile_dimension()[0]+20)
        self.image = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','spirites','eyes.png')).convert_alpha(),size)
        self.rect = self.image.get_rect(center = start_position)
        self._strategy = Eaten(self)
        self.speed = 10
        self.ghost_num = ghost_num
        self.got_to_cage = False


