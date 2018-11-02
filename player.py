from turtle import Turtle
from constants import *
import winsound

class Player(Turtle):

    def __init__(self, coord, kb):
        Turtle.__init__(self)
        
        self.speed(0)
        self.penup()
        
        self.shape("img/player.gif")
        self.seth(90)
        
        self.step_size = PLAYER_SPEED
        self.health = PLAYER_HEALTH
        
        self.score = 0

        self.setx(coord[0])
        self.sety(coord[1])
        self.kb = kb
        
    def is_inside(self, x):
        return (abs(x) + (PLAYER_LENGTH / 2)) < BORDER
    
        
    def get_left_x(self):
        return self.xcor() - PLAYER_LENGTH / 2
    
    def get_right_x(self):
        return self.xcor() + PLAYER_LENGTH / 2

    def left_move(self):
        tempx = self.xcor() - self.step_size

        if self.is_inside(tempx):
            self.setx(tempx)

    def right_move(self):
        tempx = self.xcor() + self.step_size

        if self.is_inside(tempx):
            self.setx(tempx)
  
    def miss(self):
        print("Miss!")
        winsound.PlaySound('sound/oof.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        if self.health == 1:
            return True
        else:
            self.health -= 1
            return False
    
    def update(self):
        # Handle keyboard input
        if self.kb.is_pressed("left"):
            self.left_move()
        elif self.kb.is_pressed("right"):
            self.right_move()
            