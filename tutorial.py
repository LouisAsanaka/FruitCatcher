from fruit import Fruit
from constants import *

import random

class Tutorial:
    
    @staticmethod
    def get_random_x():
        # Get a random number from the left edge to the right edge
        number = random.randint(-BORDER + FRUIT_SIZE, BORDER - FRUIT_SIZE)
        return number
    
    @staticmethod
    def raining_fruits(level):
        # LIST of fruits to rain
        fruits_to_rain = []
        for number in range(1):
            fruits_to_rain.append(Tutorial.choose_fruit(level))
        return fruits_to_rain
    
    @staticmethod
    def choose_fruit(level):
        list_of_fruits = ["apple", "grape", "pear", "orange", "banana"]
        random_x = Tutorial.get_random_x()
        return Fruit(random_x, random.choice(list_of_fruits), SPEED_DATA[level])       