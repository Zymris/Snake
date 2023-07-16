import pygame
from Constants import *

class Display():
    
    def __init__(self,snake,rule):
        self.snake = snake
        self.rule = rule
        self.display = pygame.display.set_mode((WIDTH,HEIGHT))
        self.game_caption = pygame.display.set_caption("Game of snake")
        self.message_font_style = pygame.font.SysFont(None, MESSAGE_FONT_SIZE)
        self.score_font_style = pygame.font.SysFont(None, SCORE_FONT_SIZE)
        self.highest_score_font_style = pygame.font.SysFont(None, HIGHEST_SCORE_FONT_SIZE)
        
    def update(self):
        pygame.display.update()
    
    def draw_grid(self):
        number_verti_line = WIDTH // BLOCK
        number_horiz_line = HEIGHT // BLOCK
        for verti_line in range(0,number_verti_line):
            pygame.draw.line(self.display,GRID_COLOR,(verti_line*BLOCK,0),(verti_line*BLOCK,HEIGHT))
        for horiz_line in range(0,number_horiz_line):
            pygame.draw.line(self.display,GRID_COLOR,(0,horiz_line*BLOCK),(WIDTH,horiz_line*BLOCK))       
            
    def fill(self):
        self.display.fill(BACKGROUND_COLOR)
        
    def draw_snake(self):
        for block in self.snake.snake_body:
            pygame.draw.rect(self.display,SNAKE_COLOR,(*block,BLOCK,BLOCK))
        
    def draw_food(self):
        pygame.draw.circle(self.display, GREEN, (self.snake.x_food + BLOCK//2, self.snake.y_food + BLOCK//2), BLOCK * 0.45)
        pygame.draw.circle(self.display, FOOD_COLOR, (self.snake.x_food + BLOCK//2, self.snake.y_food + BLOCK//2), int(BLOCK * 0.4))
        
    def show_message(self,message):
        message_render = self.message_font_style.render(message,True,MESSAGE_COLOR) #Create a surface to display the message
        center_of_message = message_render.get_rect(center = (X_CENTER,Y_CENTER))
        self.display.blit(message_render,center_of_message)
        
    def show_score(self):
        message_render = self.score_font_style.render(f'Score : {self.rule.score}',True,SCORE_COLOR) #Create a surface to display the message
        center_of_message = message_render.get_rect(center = (X_SCORE,Y_SCORE))
        self.display.blit(message_render,center_of_message)
        
    def show_highest_score(self):
        message_render = self.score_font_style.render(f'Highest score : {self.rule.highest_score}',True,HIGHEST_SCORE_COLOR) #Create a surface to display the message
        center_of_message = message_render.get_rect(center = (X_HIGHEST_SCORE,Y_HIGHEST_SCORE))
        self.display.blit(message_render,center_of_message)
        

        
    
        
        
        
        
        
        
