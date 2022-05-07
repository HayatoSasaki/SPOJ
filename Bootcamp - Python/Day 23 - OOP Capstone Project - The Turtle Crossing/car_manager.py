from random import choice, randint, randrange
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = [3, 4, 5, 6, 7, 8]
MOVE_INCREMENT = 5

class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.setheading(180)
        self.speed = STARTING_MOVE_DISTANCE
        self.goto(randint(300, 350), randint(-230, 240))

class CarManager(Car):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.clock = 0
        self.cars = []
        for _ in range(5):
            self.cars.append(Car())

    def spawn(self):
        self.cars.append(Car())

    def move(self):
        self.clock += 1
        if self.clock % 10 == 0:
            self.spawn()
        for _ in self.cars:
            _.forward(choice(STARTING_MOVE_DISTANCE) + (self.level * MOVE_INCREMENT))
            if _.xcor() <= -500:
                _.goto(500, _.ycor())

    def levelup(self):
        self.level += 1

    def hit(self, player):
        for _ in self.cars:
            if _.distance(player) < 20:
                return True