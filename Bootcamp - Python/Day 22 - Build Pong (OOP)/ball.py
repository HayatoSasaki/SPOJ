from random import randint
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.speed('fastest')
        self.color('white')
        self.penup()

        self.move_speed = 0.1
        self.movement = [-10, 10]

    def move(self):
        self.goto(self.xcor() + self.movement[0], self.ycor() + self.movement[1])

    def hit(self, axis):
        if axis == 'X':
            self.movement[0] *= -1
            self.move_speed *= 0.9
            self.move()
        if self.ycor() > 280 or self.ycor() < -280:
            self.movement[1] *= -1
            self.move_speed *= 0.9
            self.move()
        if self.xcor() > 380 or self.xcor() < -380:
            return True

    def reset(self):
        self.movement[0] *= -1
        self.goto(0, randint(-200, 200))