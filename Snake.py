from Constants import *
import pygame
import random 

class Snake:
    def __init__(self):
        self.snake_body = [(X_SNAKE,Y_SNAKE)]
        self.x_snake_change = X_SNAKE_CHANGE
        self.y_snake_change = Y_SNAKE_CHANGE
        self.x_food = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK # Place the food on the nearest multiple of "BLOCK" to ensure that it's aligned
        self.y_food = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK
        self.current_direction = ""
                            
    # Check for the arrow key input, and change the value of the change variable accordingly, ready to be use in the move method
    def move(self,event):
        if event.key == pygame.K_LEFT and self.current_direction != "RIGHT":
            self.current_direction = "LEFT"
            self.x_snake_change = -BLOCK
            self.y_snake_change = 0
        elif event.key == pygame.K_RIGHT and self.current_direction != "LEFT":
            self.current_direction = "RIGHT"            
            self.x_snake_change = BLOCK
            self.y_snake_change = 0
        elif event.key == pygame.K_UP and self.current_direction != "DOWN":
            self.current_direction = "UP"            
            self.x_snake_change = 0
            self.y_snake_change = -BLOCK
        elif event.key == pygame.K_DOWN and self.current_direction != "UP":
            self.current_direction = "DOWN"            
            self.x_snake_change = 0
            self.y_snake_change = BLOCK
    

        
            
        
            
    
     
        
        
        