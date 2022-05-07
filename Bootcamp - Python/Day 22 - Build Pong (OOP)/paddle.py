from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if player == 'L': # Left Paddle = Player.
            self.goto(-350, 0)
        elif player == 'R': # Right Paddle = Computer.
            self.goto(350, 0)

        self.mode = True # True = Going Up | False = Going Down.

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def automove(self):
        if self.mode and self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + 30)
            if self.ycor() >= 240:
                self.mode = False
        elif not self.mode and self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - 30)
            if self.ycor() <= -240:
                self.mode = True