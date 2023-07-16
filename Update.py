import random
from Constants import *

class Update():
    
    def __init__(self,snake=None,rule=None):
        self.snake = snake
        self.rule = rule
        
    def set_rule(self,rule):
        self.rule = rule
        
    # Here we update the new position of the Snake as the sum of the original position and the position after the player input 
    def update_snake_position(self):
        new_head = (self.snake.snake_body[0][0] + self.snake.x_snake_change, self.snake.snake_body[0][1] + self.snake.y_snake_change) 
        self.snake.snake_body.insert(0, new_head)
    
    # Update the position of the food
    def update_food_position(self):
        while True:
            self.snake.x_food = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK
            self.snake.y_food = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK
            food_position = (self.snake.x_food, self.snake.y_food)

            if food_position not in self.snake.snake_body:  # Check if food appears on the snake body
                break  # if not, we break the loop and have a valid food position
    
    def update_highest_score(self):
        if self.rule.score > self.rule.highest_score:
            print("hupdating Highest score...")
            self.rule.highest_score = self.rule.score
            with open(HIGHEST_SCORE_PATH,'w') as file:
                file.write(str(self.rule.highest_score))
            
            
    # Reset the position of the snake and the direction key pressed to start a new game
    def reset_position(self):
        self.snake.snake_body = [(X_SNAKE,Y_SNAKE)]
        self.snake.x_snake_change = X_SNAKE_CHANGE
        self.snake.y_snake_change = Y_SNAKE_CHANGE
        self.update_food_position()
        self.snake.current_direction = ""
        self.rule.score = 0

