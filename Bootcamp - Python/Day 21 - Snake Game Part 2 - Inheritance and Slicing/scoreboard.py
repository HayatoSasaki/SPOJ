from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def gameover(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=('Arial', 40, 'normal'))
