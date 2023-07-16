from Constants import *
import random

class Rule:
    def __init__(self,snake = None,update = None):
        self.snake = snake
        self.update = update
        self.score = 0
        try:
            with open(HIGHEST_SCORE_PATH,'r') as file:
                self.highest_score = int(file.read())
        except FileNotFoundError:
            self.highest_score = 0
                
    def set_update(self,update):
        self.update = update
    
    #Check if the current position of the snake is not in the boundaries of the display
    def check_if_wall_or_tail(self):
        if (self.snake.snake_body[0][0] >=  WIDTH or self.snake.snake_body[0][0] < 0 or 
            self.snake.snake_body[0][1] >= HEIGHT or self.snake.snake_body[0][1] < 0 or 
            len(self.snake.snake_body) > 1 and self.snake.snake_body[0] in self.snake.snake_body[1:]):  # Add a check for collision with itself
            game_over = True
            DEAD_SOUND.play()           
        else:
            game_over = False
            
        return game_over
    # Check if the snake is a the same position as the food
    def check_if_food_eaten(self):
        if self.snake.snake_body[0] == (self.snake.x_food, self.snake.y_food):
            random.choice(EATING_SOUND).play()
            self.update.update_food_position()
            self.score += 1
        else:
            self.snake.snake_body.pop()


    
