#Goal is to create a snake game using pygame

#Import pygame and init
import pygame
pygame.init()

#Import class and constants
from Constants import *
from Snake import Snake
from Display import Display
from Rule import Rule
from Update import Update
from State import State 

#Class init
snake = Snake()
rule = Rule(snake)
update = Update(snake)
display = Display(snake,rule)
state = State(rule, update,display)

#Set for cyclic dependency
rule.set_update(update)
update.set_rule(rule)

# Main loop
running = True
start_menu = True
start_play = False
replay_menu = False
game_over = False

while running:
    
    while start_menu:
        state.handle_start_menu()
        start_menu = False
        STARTING_SOUND.play()
        
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            snake.move(event)
            
    game_over = rule.check_if_wall_or_tail()
    
    if game_over:
        state.handle_game_over()
        replay_menu = True

    else :  
        state.handle_game()
    
    while replay_menu:
        state.handle_replay_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    running = False
                    replay_menu = False
                if event.key == pygame.K_y:
                    game_over = False
                    update.reset_position()
                    replay_menu = False
                    STARTING_SOUND.play()

#End                                         
pygame.quit()
quit()

