# SNAKE GAME PROJECT
import time
from snake import Snake
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
# PART I
# Create a snake body.
snake = Snake()
# Move the snake.
game = True
while game:
    time.sleep(0.1)
    screen.update()
    snake.move()
# Control the snake.
    screen.listen()
    screen.onkey(snake.turnleft, 'a')
    screen.onkey(snake.turnright, 'd') 
# PART II
# Detect colission with food. | Generate a new food when consumed.

# Create a scoreboard.

# Detect collision with wall.

# Detect collision with tail.

screen.exitonclick()