import time
from Constants import *
import pygame


class State:
    def __init__(self,rule,update,display):
        self.rule = rule
        self.update = update 
        self.display = display
        self.clock = pygame.time.Clock()
        
    def handle_game_over(self):
        self.display.fill()
        self.display.draw_snake()
        self.display.show_score()
        self.display.show_message(LOST_MESSAGE)
        self.display.update()
        self.update.update_highest_score()
        time.sleep(1.5)
        
    def handle_start_menu(self):
        self.display.fill()
        self.display.show_message(TITLE_MESSAGE)
        self.display.update()
        time.sleep(2)
        
        
    def handle_game(self):
        self.update.update_snake_position()
        self.display.fill()
        self.display.draw_grid()
        self.display.draw_snake()
        self.display.draw_food()
        self.display.show_score()
        self.display.update()
        self.clock.tick(SNAKE_SPEED)
        self.rule.check_if_food_eaten()        
        
    def handle_replay_menu(self):
        self.display.fill()
        self.display.show_message(REPLAY_MESSAGE)
        self.display.show_score()
        self.display.show_highest_score()
        self.display.update()        