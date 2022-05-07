from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-210, 250)
        self.write(f'Score: {self.score}', align='center', font=FONT)
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='center', font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=FONT)