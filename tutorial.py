from fruit import Fruit
from constants import *

import random

class Tutorial:
    
    @staticmethod
    def get_random_number(min_, max_):
        return random.randint(min_, max_)
    
    @staticmethod
    def get_random_x():
        # Get a random number from the left edge to the right edge
        return Tutorial.get_random_number(-BORDER + FRUIT_SIZE, BORDER - FRUIT_SIZE)
    
    @staticmethod
    def raining_fruits(level):
        # LIST of fruits to rain
        fruits_to_rain = []
        
        # Number of fruits to drop
        for number in range(FRUIT_RAIN_COUNT):
            fruits_to_rain.append(Tutorial.choose_fruit(level))

        # Random chance of a bomb drop
        if Tutorial.get_random_number(1, BOMB_DROP_CHANCE) is 2:
            fruits_to_rain.append(Tutorial.drop_bomb(level))
        return fruits_to_rain
    
    @staticmethod
    def drop_bomb(level):
        return Fruit(Tutorial.get_random_x(), "bomb", SPEED_DATA[level] + 1.5)

    @staticmethod
    def choose_fruit(level):
        list_of_fruits = ["apple", "grape", "pear", "orange", "banana"]
        random_x = Tutorial.get_random_x()
        return Fruit(random_x, random.choice(list_of_fruits), SPEED_DATA[level])       