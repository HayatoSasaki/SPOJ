import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

turtles = []
color = ['blue', 'red', 'pink', 'green', 'black', 'yellow']
pos_y = [-70, -40, -10, 20, 50, 80]    

for _ in range(6):
    turtles.append(Turtle(shape='turtle'))
    turtles[_].color(color[_])
    turtles[_].penup()
    turtles[_].goto(-230, pos_y[_])

bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color:")

race = True
while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            if turtle.color() == bet.lower():
                print(f"You've won! The {turtle.color()} turtle is the winner!")
            else:
                print(f"You've lost... The {turtle.color()} turtle is the winner!")
                
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()