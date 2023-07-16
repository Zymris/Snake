#Import
import os

#Path
MAIN_PATH = os.path.dirname(__file__)  # Path of current directory

#Color constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ELECTRIC_BLUE = (49, 55, 253)
ORANGE = (255,165,0)
DARK_GREY = (50,50,50)
LIGHT_GREY = (211,211,211)

#Display colors
BACKGROUND_COLOR = DARK_GREY
GRID_COLOR = LIGHT_GREY
SNAKE_COLOR = BLUE
FOOD_COLOR = RED

#Screen pixel Constants
WIDTH = 800
HEIGHT = WIDTH
X_CENTER = WIDTH/2
Y_CENTER = HEIGHT/2

#Snake position constants
X_SNAKE = WIDTH/2
Y_SNAKE = HEIGHT/2
X_SNAKE_CHANGE = 0
Y_SNAKE_CHANGE = 0

#Snake and food block size
BLOCK = int(((WIDTH+HEIGHT)/2)/20)

#Snake speed
SNAKE_SPEED = 20

#Message
MESSAGE_FONT_SIZE = int(((WIDTH + HEIGHT)/2)*(15/100))
MESSAGE_COLOR = ORANGE
LOST_MESSAGE = 'You lost'
REPLAY_MESSAGE = 'Play again ? (Y/N)'
TITLE_MESSAGE = 'Snake'

#Score 
SCORE_COLOR = ORANGE
SCORE_FONT_SIZE = int(((WIDTH + HEIGHT)/2)*(7.5/100))
X_SCORE = WIDTH * 0.85
Y_SCORE = HEIGHT * 0.075

#Highest score
HIGHEST_SCORE_PATH = os.path.join(MAIN_PATH, 'Highest_score.txt')
HIGHEST_SCORE_FONT_SIZE = int(((WIDTH + HEIGHT)/2)*(10/100))
HIGHEST_SCORE_COLOR = ORANGE
X_HIGHEST_SCORE = WIDTH * 0.5
Y_HIGHEST_SCORE = HEIGHT * 0.7

#Sound
from pygame import mixer

EATING_SOUNDS_FILE = ['zapsplat_cartoon_bite_munch_001_13092.mp3',
               'zapsplat_cartoon_bite_munch_002_13093.mp3',
               'zapsplat_cartoon_bite_munch_003_13094.mp3',
               'zapsplat_cartoon_bite_munch_004_13095.mp3']
EATING_SOUND = [mixer.Sound(os.path.join(MAIN_PATH, 'Sound', file)) for file in EATING_SOUNDS_FILE]

STARTING_SOUND_FILE = 'esm_5_wickets_sound_fx_arcade_casino_kids_mobile_app.mp3'
STARTING_SOUND = mixer.Sound(os.path.join(MAIN_PATH, 'Sound', STARTING_SOUND_FILE))

DEAD_SOUND_FILE = 'esm_8_bit_game_over_2_arcade_80s_simple_alert_notification_game.mp3'
DEAD_SOUND = mixer.Sound(os.path.join(MAIN_PATH, 'Sound', DEAD_SOUND_FILE))    

