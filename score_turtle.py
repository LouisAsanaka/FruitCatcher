from turtle import Turtle

class ScoreTurtle(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        
        self.speed(0)
        self.penup()
        self.hideturtle()
        
    def update_score(self, score, speed):
        self.clear()
        self.color("blue")
        self.goto(300, 200)
        self.write("Score: " + str(score) + "\nSpeed: " + str(speed), font=("Arial bold", 24), align="center")
        
    def game_over(self):
        self.color("blue")
        self.goto(0, 250)
        self.write("GAME OVER", font=("Arial bold", 30), align="center")