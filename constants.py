# -----------------------------------------------------
# You can change these
# Pixels per milliseconds
# Player Stuff
PLAYER_SPEED = 15
# Player health (# of misses player can have)
PLAYER_HEALTH = 3

# Fruit stuff
FRUIT_ACCELERATION = 0.1
# Number of fruit to rain each time
FRUIT_RAIN_COUNT = 1
# Score you get per fruit
SCORE_PER_FRUIT = 1
# Chance to drop a bomb
# Ex: 4 means 25%, 1 in 4 chance
BOMB_DROP_CHANCE = 4

# Level stuff
# How many fruits to level up?
LEVEL_UP_SCORE = 2
# Time between fruit drops as level increases
DROP_DATA = [
    2.8, 2.8, 2.5, 2.5, 2.5,
    2.5, 2, 2, 2, 2,
    1.8, 1.8, 1.5, 1.5, 1.2,
    1, 1, 1, 1, 0.5, 0.4
]
# Speed of the fruit as level increases
SPEED_DATA = [
    0.8, 0.8, 1, 1, 1,
    1.2, 1.2, 1.2, 1.5, 1.5,
    1.8, 1.8, 2, 2, 2,
    2.2, 2.2, 2.2, 2.4, 2.4,
    2.5, 2.5, 2.5, 3, 3.5
]
# -----------------------------------------------------
# Don't touch these!
WINDOW_LENGTH = 1000
WINDOW_HEIGHT = 700
BORDER = WINDOW_LENGTH / 2
LEFT_EDGE = -BORDER
RIGHT_EDGE = BORDER
TOP_EDGE = WINDOW_HEIGHT / 2
BOTTOM_EDGE = -WINDOW_HEIGHT / 2
PLAYER_LENGTH = 130
PLAYER_HEIGHT = 140
FRUIT_SIZE = 70