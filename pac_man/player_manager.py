import pygame
class PlayerManager:
    def __init__(self):
        self.__player = pygame.sprite.GroupSingle()
    
    def add_pacman(self, pacman):
        self.__player.add(pacman)

    def get_pacman(self):
        return self.__player.sprite

    def update(self):
        self.__player.update()
    @property
    def score(self):
        return self.__player.sprite.get_score()

    def draw(self, screen):
        self.__player.draw(screen)

    def delete_player(self):
        self.__player.empty()
    
    def lives(self):
        return self.__player.sprite.lives()
    
    def starting_animation(self):
        self.__player.sprite.start()
    
    def set_pacman_dead(self):
        self.__player.sprite.dead = True
    
    def is_pacman_dead(self):
        return self.__player.sprite.dead
    
    def is_power_up_active(self):
        return self.__player.sprite.is_powerup_activated()

    def disable_powerup(self):
        self.__player.sprite.disable_powerup()
