import pygame
import copy
from level import levels
from math import pi
from enum import Enum
import numpy as np
# 0 = empty black rectangle, 1 = dot, 2 = big dot, 3 = vertical line,
# 4 = horizontal line, 5 = top right, 6 = top left, 7 = bot right, 8 = bot left
# 9 = gate
class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    def __int__(self):
        return self.value

    def inverse(self):
        if self == Direction.LEFT   : return Direction.RIGHT
        elif self == Direction.RIGHT: return Direction.LEFT
        elif self == Direction.UP   : return Direction.DOWN
        elif self == Direction.DOWN : return Direction.UP

class Board:
    def __init__(self, level:int) -> None:
        self.__number_of_levels = len(levels)
        self.__level = copy.deepcopy(levels[level])
        
        
        #creating screen:
        dimensions = (len(self.__level[0]), len(self.__level[0][0]))     #33, 30  
        #To determine tile_dimension: Game_screen height <=700, width is adjusted accordingly 
        self.__tile_height = 700//dimensions[0]
        self.__tile_width = self.__tile_height 
        width, height = self.__tile_width*dimensions[1], self.__tile_height*dimensions[0] 
        self.__rect = pygame.Rect(10, 10, width, height)  # dimensions do not matter since board will adjust them
        self.__game_screen = pygame.Surface((width, height))
        self.__i = 0


    def get_screen(self):
        return self.__game_screen
    
    def get_rect(self):
        return self.__rect
    
    def get_string_position(self):
        tup = self.__level[5]
        return (tup[1] *self.__tile_width, tup[0]*self.__tile_height)
    
    def get_out_position(self):
        return (self.__level[3][1],self.__level[3][0])
    def get_eyes_back_position(self):
        return (self.__level[4][1],self.__level[4][0])

    def manhatan_distance(self, position1, position2):
        return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])
    
    # def euclidean(self, position1, position2):
    #     return (position1[0]- position2[0])**2 + (position1[1]- position2[1])**2 

    def check_if_won(self):
       return np.all(~np.isin(self.__level[0], [1, 2]))
    
    def number_of_levels(self):
        return self.__number_of_levels

    def tunneling(self, position): 
        dimensions = (len(self.__level[0]), len(self.__level[0][0]))
        
        if position[0] < self.__tile_width+self.__tile_width//3:
            new_x = (dimensions[1]-1.5)*self.__tile_width
        elif position[0] > (dimensions[1]-1.5)*self.__tile_width:
            new_x = self.__tile_width+self.__tile_width//2
        else: new_x = position[0]

        return new_x, position[1]
            
    
    def possible_moves(self, position:tuple, speed, direction, num = 2):
        # num is the parameter that determines if a sprite can go through the gate

        # i,j are the tile coordinates
        i,j = position[1]//self.__tile_height, position[0]//self.__tile_width
        lvl = self.__level[0]
        margin = speed + 1

        # We need to consider horizontal and vertical movement separately
        # since we need to account for turning so the pacman can't turn if 
        # it is one pixel into the next tile

        if direction == Direction.LEFT or direction == Direction.RIGHT:
            if direction == Direction.LEFT:
                left = True if lvl[i][j-1]<=num else (True if position[0] > j*self.__tile_width + margin else False)
                right = lvl[i][j+1]<=num

            elif direction == Direction.RIGHT:
                left = lvl[i][j-1] <=num
                right = True if lvl[i][j+1]<=num else (True if position[0] < j*self.__tile_width - margin else False)

            up = (lvl[i-1][j]<=num and position[0] < j*self.__tile_width + 2*margin)
            down =  (lvl[i+1][j] <=num and position[0] < j*self.__tile_width + 2*margin)    
        
        elif direction == Direction.DOWN or direction == Direction.UP:
            if direction == Direction.UP:
                up = True if lvl[i-1][j]<=num else (True if position[1] > i*self.__tile_height +margin else False)
                down = lvl[i+1][j]<=num
            
            elif direction == Direction.DOWN:
                up = lvl[i-1][j]<=num 
                down = True if lvl[i+1][j]<=num else (True if position[1] < i*self.__tile_height - margin else False)
            
            left = (lvl[i][j-1]<=num and position[1] < i*self.__tile_height + 2*margin)
            right = (lvl[i][j+1]<=num and position[1] < i*self.__tile_height + 2*margin)

        return [left, right, up, down]
             
    def get_value(self, index1:int, index2 :int) -> int:
        return self.__level[0][index1][index2]
    
    def erase_value(self, index1:int, index2:int) -> None:
        self.__level[0][index1][index2] = 0

    def pac_man_start_position(self):
        return ((self.__level[1][1] )*self.__tile_width, (self.__level[1][0] )*self.__tile_height)

    def ghost_start_position(self):
        positions = self.__level[2]
        return [((pos[1])*self.__tile_width, (pos[0])*self.__tile_height) for pos in positions]

    def tile_dimension(self):        
        return (self.__tile_width, self.__tile_height)
    
    


    def draw(self, to_blink:bool = False) -> None:

        level = self.__level[0]
        line_width = 5
        
        wall_color, coin_color, gate_color, blink_color = self.__level[6]
         
        if to_blink:
            if self.__i% 40 < 20:
                wall_color = blink_color
            self.__i +=1
            if self.__i == 40: self.__i = 0

        # the offset 0.5 is due to the fact that I want the boundaries match the tile boundaries
        # uncomment the debbug grid to see 
        for i in range(len(level)):
            for j in range(len(level[0])):
                s = i - 0.5
                k = j - 0.5
                if level[i][j] == 1:
                    small_radius = 0.4 * (self.__tile_width//2)
                    pygame.draw.circle(self.__game_screen, coin_color, ((k+0.5)*self.__tile_width, (s+0.5)*self.__tile_height), small_radius)              
                if level[i][j] == 2:
                    radius = 0.7 *(self.__tile_width//2)
                    pygame.draw.circle(self.__game_screen, 'red', ((k+0.5)*self.__tile_width, (s+0.5)*self.__tile_height), radius)
                if level[i][j] == 3:
                    pygame.draw.line(self.__game_screen, gate_color, (k* self.__tile_width, (s+0.5)* self.__tile_height), ((k+1)* self.__tile_width, (s+0.5)* self.__tile_height), line_width)
                if level[i][j] == 4:
                    pygame.draw.line(self.__game_screen, wall_color, ((k+0.5)* self.__tile_width, s* self.__tile_height), ((k+0.5)* self.__tile_width, (s+1)* self.__tile_height), width = line_width)
                if level[i][j] == 5:
                    pygame.draw.line(self.__game_screen, wall_color, (k* self.__tile_width, (s+0.5)* self.__tile_height), ((k+1)* self.__tile_width, (s+0.5)* self.__tile_height), width = line_width)
                if level[i][j] == 6:
                    #we need to have a larger rectangle than the tile to match since the pi/2 is not on the left end
                    rectangle = ((k-0.5)* self.__tile_width, (s+0.5)*self.__tile_height, self.__tile_width, self.__tile_height)
                    pygame.draw.arc(self.__game_screen, wall_color, rectangle, start_angle=0, stop_angle= pi/2, width = line_width)
                if level[i][j] == 7:
                    rectangle = ((k+0.5)* self.__tile_width, (s+0.5)*self.__tile_height, self.__tile_width, self.__tile_height)
                    pygame.draw.arc(self.__game_screen, wall_color, rectangle, start_angle=pi/2, stop_angle= pi, width = line_width)
                if level[i][j] == 8:
                    rectangle = ((k-0.5)* self.__tile_width, (s-0.5)*self.__tile_height, self.__tile_width, self.__tile_height)
                    pygame.draw.arc(self.__game_screen, wall_color, rectangle, start_angle=-pi/2, stop_angle= 0, width = line_width)
                if level[i][j] == 9:
                    rectangle = ((k+0.5)* self.__tile_width, (s-0.5)*self.__tile_height, self.__tile_width, self.__tile_height)
                    pygame.draw.arc(self.__game_screen, wall_color, rectangle, start_angle=pi, stop_angle=-pi/2, width = line_width)

        # TILE Drawing for debugging purposes  (DEBUG grid) 
        # font = pygame.font.Font(None, 20)

        # for i in range(len(level)+1):
        #     text_surface = font.render(f"{i}", True, 'green')
        #     self.__game_screen.blit(text_surface, (0,i*self.__tile_height))
        #     pygame.draw.line(self.__game_screen,'green' ,(0,i*self.__tile_height), (self.__game_screen.get_size()[0], i*self.__tile_height ))
        # for j in range(len(level[0])):
        #     text_surface = font.render(f"{j}", True, 'green')
        #     self.__game_screen.blit(text_surface, (j*self.__tile_width, 0))
        #     pygame.draw.line(self.__game_screen,'green', (j*self.__tile_width, 0), (j*self.__tile_width, self.__game_screen.get_size()[1] ))            


        
        


