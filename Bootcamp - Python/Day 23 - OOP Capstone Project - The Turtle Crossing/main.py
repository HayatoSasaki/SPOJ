import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
car = CarManager()
player = Player()
screen.listen()
screen.onkey(player.move, 'Up')

game = True
while game:
    time.sleep(0.1)
    screen.update()
    car.move()

    if player.win():
        car.levelup()
        score.update()
    
    if car.hit(player):
        game = False
        score.gameover()

screen.exitonclick()