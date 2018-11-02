import turtle

from constants import *
from player import Player
from arena import Arena
from score_turtle import ScoreTurtle
from fruit import Fruit
from keyboard import Keyboard

# Create the screen
screen = turtle.Screen()
# Get the canvas
canvas = turtle.getcanvas()
# Create a keyboard
kb = Keyboard(canvas)

# Setup the game!
def setup():
    # Save some memory
    turtle.setundobuffer(None)
    # Create the window
    turtle.setup(WINDOW_LENGTH, WINDOW_HEIGHT)
    # Hide the default turtle
    turtle.hideturtle()
    # Change the background color
    screen.bgcolor("white")
    # Set the window title
    screen.title("Fruit Catcher")
    # Turn on manuel draw mode for more control
    screen.tracer(False)
    # Remove the window borders
    canvas.config(borderwidth=0, highlightthickness=0)
    
def register_shapes():
    turtle.addshape("img/apple.gif")
    turtle.addshape("img/grape.gif")
    turtle.addshape("img/player.gif")

player = None
PLAYER_TOP_Y = 0
def create_player():
    global player, PLAYER_TOP_Y
    
    player = Player((0, BOTTOM_EDGE + 80), kb)
    PLAYER_TOP_Y = player.ycor() + PLAYER_HEIGHT / 2
    
    kb.register_key("a", "left")
    kb.register_key("d", "right")
    
    turtle.listen()

score = ScoreTurtle()
def draw():
    for entity in screen.turtles():
        if isinstance(entity, Fruit):
            update = entity.update()
            if update is not None:
                gameover = False
                if entity.get_bottom_y() < PLAYER_TOP_Y:
                    if (player.get_left_x() < entity.get_left_x() < player.get_right_x() or
                        player.get_left_x() < entity.get_right_x() < player.get_right_x()):
                        player.score += 1
                        if (player.score % 2 is 0):
                            global current_speed
                            if not (current_speed < 0.5):
                                current_speed *= DROP_SPEED_MULTIPLIER
                        score.update_score(player.score, round(current_speed, 2))
                        entity.despawn()
                    elif update is False:
                        print("Fail")
                        gameover = player.miss()
                if gameover is True:
                    score.game_over()
                    canvas.after_cancel(task_id)
                    return
    player.update()

    # Draw the objects on the screen!
    screen.update()
    # Redraw every 20 milliseconds
    canvas.after(20, draw)

task_id = None
current_speed = INITIAL_DROP_SPEED
def spawn_fruits():
    global task_id, current_speed
    Tutorial.raining_fruits()
    task_id = canvas.after(int(current_speed * 1000), spawn_fruits)

setup()
register_shapes()

game_arena = Arena()
game_arena.draw_arena()
score.update_score(0, current_speed)
create_player()

from tutorial import Tutorial
draw()
spawn_fruits()

# Required for every turtle program
turtle.mainloop()