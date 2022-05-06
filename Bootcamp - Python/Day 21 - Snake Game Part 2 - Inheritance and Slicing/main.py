# SNAKE GAME PROJECT
import time
from snake import Snake
from food import Food
from scoreboard import Score
from turtle import Turtle, Screen, xcor, ycor

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# PART I
# Create a snake body.
snake = Snake()
score = Score()
food = Food()

# Control the snake.
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right') 

# Move the snake.
score.update()
game = True
while game:
    time.sleep(0.1)
    screen.update()
    snake.move(20)

# PART II
# Detect colission with food. 
    if snake.head.distance(food) < 15:
        snake.feed(1)
        food.respawn()
        score.update()

# Detect collision with wall and Detect collision with tail.
    if snake.dead() or snake.ouroboros():
        game = False
        score.gameover()

screen.exitonclick()