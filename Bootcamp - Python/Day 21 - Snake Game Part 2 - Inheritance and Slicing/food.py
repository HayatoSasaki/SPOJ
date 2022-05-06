from importlib import import_module
from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.color('blue')
        self.penup()

        self.respawn()

    def respawn(self):
        self.goto(randint(-280, 280), randint(-280, 280))