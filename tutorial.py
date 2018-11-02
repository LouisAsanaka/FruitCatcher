from fruit import Fruit
from constants import *

import random

class Tutorial:
    
    @staticmethod
    def get_random_x():
        return random.randint(-BORDER + FRUIT_SIZE, BORDER - FRUIT_SIZE)
    
    @staticmethod
    def raining_fruits():
        fruits_to_rain = []
        for number in range(1):
            fruits_to_rain.append(Tutorial.choose_fruit())
        return fruits_to_rain
    
    @staticmethod
    def choose_fruit():
        list_of_fruits = ["apple", "grape"]
        random_x = Tutorial.get_random_x()
        return Fruit(random_x, random.choice(list_of_fruits))       