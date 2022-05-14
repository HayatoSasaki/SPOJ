from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('Bootcamp - Python/Day 24/Snake w Highscore/data.txt') as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('Bootcamp - Python/Day 24/Snake w Highscore/data.txt', 'w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()