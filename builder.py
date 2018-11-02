from turtle import Turtle
from constants import *

class Builder(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        
        # Make the builder turtle super fast!
        self.speed(0)
        
    def draw_arena_outline(self):
        # Don't draw when moving!
        self.penup()
        # Teleport the builder to this position
        self.goto(LEFT_EDGE, TOP_EDGE)
        # Start drawing the lines!
        self.pendown()
        # Change the thickness of the line
        self.pensize(5)
        # Set the color of the line
        self.color("green")
        # Four sides of a square
        for count in range(2):
            # Move forward
            self.forward(WINDOW_LENGTH - 7)
            # Turn right
            self.right(90)
            self.forward(WINDOW_HEIGHT - 7)
            self.right(90)

        # Hide the builder turtle
        self.hideturtle()