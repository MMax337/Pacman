from board import Board
from pacman import PacMan
from player_manager import PlayerManager
from ghost_manager import GhostMangaer
from display_manager import DisplayManager
from game_logic import GameLogic
from keyboard_manager import KeyManager


class GameManager:
    def __init__(self):
        self.__level = 1
        self.__board = Board(self.__level)
        self.__score = 0
        self.__won = False
        self.__lost = False
        self.__started = True
        self.__restarting = False

        self.__player_manager = PlayerManager()
        self.__ghost_manger = GhostMangaer(self.__board)
        self.__game_logic = GameLogic(self.__board,self.__player_manager, self.__ghost_manger)
        self.__display_manager = DisplayManager(self.__board,self.__ghost_manger ,self.__player_manager)
        self.__key_manager = KeyManager()
        self.__player_manager.add_pacman(PacMan(self.__board, self.__key_manager, 0))
        self.__ghost_manger.ghost_fill()
        #All initialization of PacMan and ghost classes should be only after display manager was initialized
        
    def game_over(self):
        self.__player_manager.delete_player()
        self.__ghost_manger.delete_ghosts()
        self.__lost = True
    

    def next_level(self):
        self.__level += 1
        lives = self.__player_manager.lives()
        self.__player_manager.delete_player()
        self.__ghost_manger.delete_ghosts()
        self.start(self.__level, self.__score, lives)
    
    def start(self, level:int, score = 0, lives:int = 3, new_game = False):
        self.__level = level
        self.__board = Board(self.__level)
        self.__ghost_manger = GhostMangaer(self.__board)
        self.__ghost_manger.ghost_fill()
        self.__score = score
        self.__key_manager = KeyManager()
        self.__player_manager.add_pacman(PacMan(self.__board, self.__key_manager ,self.__score, lives))   
        self.__game_logic.reset(self.__board,self.__player_manager, self.__ghost_manger, new_game)
        self.__display_manager = DisplayManager(self.__board,self.__ghost_manger ,self.__player_manager)
        
        

        self.__won = False
        self.__lost = False
        self.__started = True
        self.__restarting = False
             

    def is_lost(self):
        return self.__lost
    def is_won(self):
        return self.__won
    def just_started(self):
        return self.__started
   
    def last_level(self):
        return self.__level == self.__board.number_of_levels()
    
    def win_check(self):
        self.__won = self.__board.check_if_won()
    
    def lives_gone(self):
        return self.__player_manager.lives() <= 0
    
    def start_restart(self):
        self.__restarting = True
    
    def restart_finish(self):
        if self.__restarting and not self.__player_manager.is_pacman_dead():
            self.__ghost_manger.ghost_fill()
            self.__restarting = False
            self.__started = True
    def update_score(self):
        self.__score = self.__player_manager.score

    def active_game(self, elapsed_time):
        self.__ghost_manger.time_update(elapsed_time)
        self.__game_logic.adjust_difficulty()
        self.__ghost_manger.get_out()
        self.__ghost_manger.follow_mode(self.__player_manager.get_pacman())
        self.__ghost_manger.random_mode()
        self.__ghost_manger.eyes_managing()
        self.__game_logic.active_powerup_logic(elapsed_time)
        
       
        self.__display_manager.display_active_game(self.__level,self.__player_manager.lives() ,self.__player_manager.score)
        self.update_score()
        collided = self.__game_logic.collisions()
        
        if collided and not self.lives_gone():
            self.start_restart()
        
        self.restart_finish()


        if self.lives_gone():
            self.game_over()

        self.win_check()
    
    def display_starting_screen(self, fps):
        self.__display_manager.display_starting_screen(fps, self.__level, self.__score)
        self.__started = self.__display_manager.just_started()

    def play_win_animation(self, fps):
        finished = self.__display_manager.play_win_animation(fps,self.__level, self.__player_manager.lives(), self.__score)
        return finished

    def display_game_over(self):
        self.__display_manager.display_game_over(self.__score)
    
    def game_won(self):
        self.__display_manager.display_game_won(self.__score)
    
    def keys_update(self):
        self.__key_manager.update()
    
    def exit(self):
        return self.__key_manager.check_for_exit()
    
    def space_bar_pressed(self):
        return self.__key_manager.check_for_space()
        
     