import pygame
from game_manager import GameManager


pygame.init()

FPS = 60
pause = False

game = GameManager()

clock = pygame.time.Clock()
#mainloop
run = True
while run:
    elapsed_time = clock.tick(FPS)
    game.keys_update()
    if game.is_lost():
        game.display_game_over()
    
    if game.is_won():
        win_animation_finished = game.play_win_animation(FPS) 
        if win_animation_finished:
            if game.last_level(): game.game_won()
            else: game.next_level() 


    if game.exit():
        pygame.quit()
        exit()
    if game.is_lost() and game.space_bar_pressed():
            game.start(level=1,new_game=True)
    if game.is_won() and game.space_bar_pressed():
        game.start(level=1, new_game=True)
    

    if game.just_started():
        game.display_starting_screen(FPS)

    if not game.is_lost() and not pause and not game.is_won() and not game.just_started():
        game.active_game(elapsed_time)
     

    pygame.display.update()
    

    
    