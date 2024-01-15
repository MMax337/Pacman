import pygame
import os

class DisplayManager:
    def __init__(self, board, ghost_manger, player):
        self.__joker_font = pygame.font.SysFont("jokerman", 30)
        self.__chiller_font = pygame.font.SysFont("Chiller", 40)
        self.__board = board
        self.__screen = pygame.display.set_mode((self.__board.get_screen().get_size()[0], self.__board.get_screen().get_size()[1] + 100))
        self.__life_icon = pygame.transform.smoothscale(pygame.image.load(os.path.join('images','pac_man','life.png')).convert_alpha(),(30,30))
        self.__game_screen = self.__board.get_screen()
        self.__ghost_manger = ghost_manger
        self.__player_manager = player
        self.__starting_animation_index = 0
        self.__win_animation = 0
        self.__started = True


    def __display_score(self, score):
        score_surf = self.__joker_font.render(f"SCORE: {score}",self.__screen,'white')
        score_rect = score_surf.get_rect(topleft = (10, 10))
        self.__screen.blit(score_surf,score_rect)

    def __display_lives(self, lives:int):
        for i in range(lives):
            life_icon_rect = self.__life_icon.get_rect(topleft = (10+40*i, self.__game_screen.get_size()[1]+50))
    
            self.__screen.blit(self.__life_icon,life_icon_rect)

    def __display_level(self, level:int):
        lvl_surf = self.__joker_font.render(f"Level: {level}",self.__screen, 'white')
        lvl_rect = lvl_surf.get_rect(topleft = ((self.__game_screen.get_size()[0]//3 + 50, 10)))
        self.__screen.blit(lvl_surf,lvl_rect)

        
    def display_starting_screen(self, fps, level, score):
        self.__started = True
        self.__screen.fill((0,0,0))
        self.__game_screen.fill((0,0,0))
        self.__board.draw()
        
        self.__player_manager.starting_animation()
        self.__player_manager.draw(self.__game_screen)
        self.__ghost_manger.draw(self.__game_screen)
        self.__display_score(score)
        self.__display_lives(self.__player_manager.lives())
        self.__display_level(level)

        self.__screen.blit(self.__game_screen, (10, 50))

        self.__starting_animation_index += 1
        if self.__starting_animation_index > 2*fps:
            self.__starting_animation_index = 0 
            self.__started = False


    def display_active_game(self, level, lives, score):
        self.__screen.fill((0,0,0))
        self.__game_screen.fill((0,0,0))
        self.__board.draw()
        self.__player_manager.update()
        self.__ghost_manger.update()

        self.__player_manager.draw(self.__game_screen)
        self.__ghost_manger.draw(self.__game_screen)

        self.__display_score(score)
        self.__display_lives(lives)
        self.__display_level(level)
        self.__screen.blit(self.__game_screen, (10, 50))



    def display_game_over(self, score):
        self.__screen.fill((0,0,0))
        self.__game_screen.fill((0,0,0))
        self.__board.draw()
        
        end_surf = self.__chiller_font.render("GAME  OVER",self.__screen,'Red')
        end_rect = end_surf.get_rect(topleft = self.__board.get_string_position())

        restart_surf = self.__chiller_font.render("Press space bar to restart",self.__screen,'white')
        restart_surf_rect = restart_surf.get_rect(topleft = (self.__game_screen.get_size()[0]//4, self.__game_screen.get_size()[1]+35))

        self.__game_screen.blit(end_surf,end_rect)
        self.__screen.blit(self.__game_screen, (10, 50))
        self.__screen.blit(restart_surf,restart_surf_rect)

        self.__display_score(score)

    
    def display_win_screen(self, level, lives, score):
        self.__screen.fill((0,0,0))
        self.__game_screen.fill((0,0,0))
        self.__board.draw(to_blink= True)

        self.__player_manager.draw(self.__game_screen)
        
        self.__screen.blit(self.__game_screen, (10, 50))
        self.__display_score(score)
        self.__display_lives(lives)
        self.__display_level(level)
    
    def play_win_animation(self, FPS, level, lives, score):
        self.__ghost_manger.delete_ghosts()
        
        if self.__win_animation < 4*FPS:
            self.__win_animation +=1
            self.display_win_screen(level, lives, score)
            return False
        #returns bool if win animation is finished
        return True

    def just_started(self):
        return self.__started
    
    def display_game_won(self, score):
        self.__screen.fill((0,0,0))
        self.__game_screen.fill((0,0,0))
        self.__board.draw()
        
        win_surf = self.__joker_font.render(f"  YOU WON",self.__screen,'Green')
        win_rect = win_surf.get_rect(topleft = self.__board.get_string_position())
        
        restart_surf = self.__chiller_font.render("Press space bar to restart",self.__screen,'white')
        restart_surf_rect = restart_surf.get_rect(topleft = (self.__game_screen.get_size()[0]//4, self.__game_screen.get_size()[1]+35))
        
        self.__game_screen.blit(win_surf,win_rect)
        self.__screen.blit(restart_surf,restart_surf_rect)
        self.__screen.blit(self.__game_screen, (10, 50))
        self.__display_score(score)
