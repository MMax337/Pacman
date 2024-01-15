import pygame
import random
from ghost import Ghost
from strategy import GetOut, Follow, Walk

class GhostMangaer:
    def __init__(self, board):
        self.__board = board
        self.__ghosts = pygame.sprite.Group()
        self.__scared_ghosts = pygame.sprite.Group()
        self.__eyes_group = pygame.sprite.Group()
        self.__get_out_time = 0
        self.__follow_mode = 0
        self.__random_walk = 0

        #numbers in miliseconds
        self.__get_out_timing = 4000
        self.__follow_timing = 4000
        self.__random_timing = 5000
        
    def add_ghost(self, ghost):
        self.__ghosts.add(ghost)

    def add_scared_ghost(self, scared_ghost):
        self.__scared_ghosts.add(scared_ghost)

    def add_eye(self, eye):
        self.__eyes_group.add(eye)
    
    def delete_ghosts(self):
        self.__ghosts.empty()
        self.__scared_ghosts.empty()
        self.__eyes_group.empty()
    
    def update(self):
        self.__ghosts.update()
        self.__scared_ghosts.update()
        self.__eyes_group.update()
    
    @property
    def scared_ghosts(self):
        return self.__scared_ghosts
    
    @property
    def ghosts(self):
        return self.__ghosts
    
    def set_timings(self, get_out, follow, random):
        self.__get_out_timing = get_out
        self.__follow_timing = follow
        self.__random_timing = random

    def ghost_fill(self):
        count = 0
        for pos in self.__board.ghost_start_position():
            self.__ghosts.add(Ghost(pos,self.__board, count !=0, count+1))
            count += 1
    
    def time_update(self, time:int):
        self.__get_out_time += time
        self.__follow_mode += time
        self.__random_walk += time

    def eyes_managing(self):
        eyes_to_remove =[]
        for eyes in self.__eyes_group:
            if eyes.got_to_cage:
                ghost_to_add = Ghost(eyes.get_position(), self.__board, True, eyes.ghost_num)
                ghost_to_add.ressurectred = True
                self.__ghosts.add(ghost_to_add)
                eyes_to_remove.append(eyes)

        for eyes in eyes_to_remove: eyes.kill()
    
    def get_out(self):
        if self.__get_out_time > random.randint(self.__get_out_timing, self.__get_out_timing+2000): #2000,4000
            for ghost in self.__ghosts:
                if ghost.inCage:
                    ghost.set_strategy(GetOut(ghost))
                    ghost.inCage = False
                    break
            for scared_ghost in self.__scared_ghosts:
                if scared_ghost.inCage:
                    scared_ghost.set_strategy(GetOut(scared_ghost))
                    scared_ghost.inCage = False
                    break
            self.__get_out_time = 0

    def follow_mode(self, pacman):
        if self.__follow_mode > random.randint(self.__follow_timing, self.__follow_timing + 1000):
            for ghost in self.__ghosts:
                if not ghost.inCage and not ghost.following and not ghost.getting_out:
                    ghost.set_strategy(Follow(ghost, pacman))
                    ghost.following = True
                    break
            self.__follow_mode = 0
    
    def random_mode(self):
        if self.__random_walk > random.randint(self.__random_timing, self.__random_timing + 2000):
            for ghost in self.__ghosts:
                if not ghost.inCage and ghost.following and not ghost.getting_out:
                    ghost.set_strategy(Walk(ghost))
                    ghost.following = False
                    break
            self.__random_walk = 0
            self.__follow_mode = 0
    
    def draw(self, screen):
        self.__ghosts.draw(screen)
        self.__scared_ghosts.draw(screen)
        self.__eyes_group.draw(screen)