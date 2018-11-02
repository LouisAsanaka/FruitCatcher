from turtle import Turtle
from constants import *

class Fruit(Turtle):
    
    def __init__(self, x, name):
        Turtle.__init__(self)
        
        self.speed(0)
        self.penup()
        self.shape("img/" + name + ".gif")
        self.setx(x)
        self.sety(TOP_EDGE)
        self.seth(270)
        
        self.step_size = 5
        self.radius = 5
        
    def is_inside(self, y):
        return (y - (FRUIT_SIZE / 2)) > -BORDER
    
    def get_left_x(self):
        return self.xcor() - FRUIT_SIZE / 2
    
    def get_right_x(self):
        return self.xcor() + FRUIT_SIZE / 2
    
    def get_bottom_y(self):
        return self.ycor() - FRUIT_SIZE / 2
    
    def despawn(self):
        print("Despawning")
        self.hideturtle()
        
    def update(self):
        if not self.isvisible():
            return
        if self.is_inside(self.ycor()):
            # Falling code
            self.sety(self.ycor() - self.step_size)
            return True
        else:
            print("Hit the bottom!")
            self.hideturtle()
            return False
