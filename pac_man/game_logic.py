from ghost import Ghost, Scared_Ghost, Eyes
from strategy import Walk, InCage, GetOut, Eaten, Follow
import pygame
import random

class GameLogic:
    def __init__(self, board,player_manager, ghost_manger):
        self.__board = board
        self.__player_manager = player_manager
        self.__ghost_manger = ghost_manger
        self.__power_up_time = 0
        self.__power_up_activated = False

        
        self.__number_of_deaths = 0
        self.__number_of_eaten_ghosts = 0
        self.__level_difficulty_scaling = 0
        self.__difficulty_points = 0

        self.__powerup_duraction = 6000
        

                
    def reset(self, board,player_manager, ghost_manger, new_game: bool):
        self.__board = board
        self.__player_manager = player_manager
        self.__ghost_manger = ghost_manger
        self.__power_up_time = 0
        self.__power_up_activated = False
        if not new_game:
            self.__level_difficulty_scaling += 7
        else:
            self.__number_of_deaths = 0
            self.__number_of_eaten_ghosts = 0
            self.__level_difficulty_scaling = 0
            self.__difficulty_points = 0

    def collisions(self):
        margin = 30
        pacman_smaller_rect = self.__player_manager.get_pacman().rect.inflate(-margin, -margin)
        collision = False

        for ghost in self.__ghost_manger.ghosts:
            collision = pacman_smaller_rect.colliderect(ghost.rect)
            if collision:
                self.__number_of_deaths += 1
                pygame.time.delay(500)
                self.__ghost_manger.delete_ghosts()
                self.__player_manager.set_pacman_dead()
                break
        
        return collision

    def __frightened_collisions(self):
        margin = 30
        # we take a smaller rectangle so we have a visible collision and not just a pixel collision
        pacman_smaller_rect = self.__player_manager.get_pacman().rect.inflate(-margin, -margin)
        
        scared_ghosts_to_remove = []
        for scared_ghost in self.__ghost_manger.scared_ghosts:
            collision = pacman_smaller_rect.colliderect(scared_ghost.rect)
            if collision:
                self.__number_of_eaten_ghosts += 1
                scared_ghost.set_strategy(Eaten(scared_ghost))
                self.__ghost_manger.add_eye(Eyes(scared_ghost.get_position(), self.__board, scared_ghost.ghost_num))
                scared_ghosts_to_remove.append(scared_ghost)
        
        for scared_ghost in scared_ghosts_to_remove: scared_ghost.kill()

    def __scare_ghosts(self, time:int):    
        self.__frightened_collisions()
        self.__power_up_time +=time
        ghosts_to_remove = []
        for ghost in self.__ghost_manger.ghosts:
            if not ghost.ressurectred:
                self.__ghost_manger.add_scared_ghost(Scared_Ghost(ghost.get_position(), self.__board, ghost.inCage,ghost.getting_out,ghost.ghost_num, self.__player_manager.get_pacman()))
                ghosts_to_remove.append(ghost)

        for ghost in ghosts_to_remove: ghost.kill()

    def __unable_power_up(self):
        self.__power_up_activated = True
        self.__power_up_time = 0
        
        for ghost in self.__ghost_manger.ghosts:
            ghost.ressurectred = False
        
        for scared_ghost in self.__ghost_manger.scared_ghosts:
            scared_ghost.blinking(False)
        self.__player_manager.disable_powerup()

    def __disable_power_up(self):        
        self.__power_up_time = 0
        self.__power_up_activated = False

        scared_ghosts_to_remove = []
        for scared_ghost in self.__ghost_manger.scared_ghosts:
                self.__ghost_manger.add_ghost(Ghost(scared_ghost.get_position(), scared_ghost.get_board(),scared_ghost.inCage, scared_ghost.ghost_num, scared_ghost.getting_out))
                scared_ghosts_to_remove.append(scared_ghost)
        
        for scared_ghost in scared_ghosts_to_remove: scared_ghost.kill()
            
        for ghost in self.__ghost_manger.ghosts:
            if ghost.inCage:
                ghost.set_strategy(InCage(ghost))
            elif ghost.getting_out:
                ghost.set_strategy(GetOut(ghost))
            else:
                if self.__difficulty_points <= 15:
                    ghost.set_strategy(Walk(ghost))
                else:
                    ghost.set_strategy(Follow(ghost, self.__player_manager.get_pacman()))
            ghost.ressurectred = False
            
    def active_powerup_logic(self, time):
        if self.__power_up_activated:
            self.__scare_ghosts(time)
        
        if self.__player_manager.is_power_up_active():
            self.__unable_power_up()
        
        if self.__power_up_time > random.randint(self.__powerup_duraction - 1000, self.__powerup_duraction - 500):
            for scared_ghost in self.__ghost_manger.scared_ghosts:
                scared_ghost.blinking(True)        

        if self.__power_up_time > random.randint(self.__powerup_duraction, self.__powerup_duraction + 1000):
            self.__disable_power_up()
    
    def adjust_difficulty(self):
        
        self.__difficulty_points = 2*self.__number_of_eaten_ghosts + self.__level_difficulty_scaling - 4 * self.__number_of_deaths 

        if self.__difficulty_points < 5: #easy
            self.__difficulty_helper(6000, 4000, 3000, 5000, 3)
        elif self.__difficulty_points <= 10: #medium
            self.__difficulty_helper(4000, 2500, 3000, 7000, 4)
        elif self.__difficulty_points <= 15: #hard
            self.__difficulty_helper(2500, 1000, 2000, 8000, 5)
        else:                               #godlike
            self.__difficulty_helper(1500, 1000, 2000, 10_000, 5)
            #Additionaly note the change in disable power_up
    
    
    def __difficulty_helper(self, powerup, get_out, follow, random, speed):
        self.__powerup_duraction = powerup
        self.__ghost_manger.set_timings(get_out, follow, random)
        for ghost in self.__ghost_manger.ghosts:
            ghost.set_speed(speed)
        

        
