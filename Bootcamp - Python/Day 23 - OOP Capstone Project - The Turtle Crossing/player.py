STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
GOAL = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(10)

    def win(self):
        if self.ycor() > GOAL:
            self.goto(STARTING_POSITION)
            return True