import pygame
from board import Direction

class KeyManager:
    def __init__(self):
        self.__events = pygame.event.get()
    
    def update(self):
        self.__events = pygame.event.get()
    
    def check_for_exit(self):
        for event in self.__events:
            if event.type == pygame.QUIT:
                return True
        return False
   
    def check_for_space(self):
        for event in self.__events:
            if  event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True
        return False

    def get_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: return Direction.LEFT 
        
        elif keys[pygame.K_RIGHT]: return Direction.RIGHT
        
        elif keys[pygame.K_UP]: return Direction.UP
        
        elif keys[pygame.K_DOWN]: return Direction.DOWN

        else: return None
    

