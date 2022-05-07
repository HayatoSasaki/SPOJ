# PONG GAME PROJECT
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

# Create the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

score = Score()

# Create and move a paddle. | Create another paddle.
paddle_L = Paddle('L') # Left Paddle = Player.
paddle_R = Paddle('R') # Right Paddle = Computer.

screen.listen()
screen.onkey(paddle_L.up, 'w') # W or 'Up'
screen.onkey(paddle_L.down, 's') # S or 'Down'

# Create a ball and make it move.
ball = Ball()

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    paddle_R.automove()    

# Detect collision with wall and bounce. | Detect colision with paddle.
    if ball.distance(paddle_R) < 50 and ball.xcor() > 320 or ball.distance(paddle_L) < 50 and ball.xcor() < -320:
        ball.hit('X')

# Detect when paddle misses. | Keep score.
    if ball.hit('Y'):
        if ball.movement[0] == 10:
            score.score_1 += 1 # Player 1 Scored.
        else:
            score.score_2 += 1 # Player 2 Scored.
        score.update()
        ball.reset()

screen.exitonclick()