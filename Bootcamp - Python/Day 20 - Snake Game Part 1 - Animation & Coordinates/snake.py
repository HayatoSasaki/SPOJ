from turtle import Turtle

class Snake:

    def __init__(self):
        self.head = Turtle(shape='square')
        self.head.color('white')
        self.head.penup()
        self.tail = []
        self.feed(2)

    def feed(self, food):
        for _ in range(food):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto((self.head.xcor()-20*(_+1), self.head.ycor()))
            self.tail.append(new_segment)

    def move(self):
        new_movement = [self.head.xcor(), self.head.ycor()]
        self.head.forward(20)
        for segment in self.tail:
            old_movement = [segment.xcor(), segment.ycor()]
            segment.goto(new_movement)
            new_movement = old_movement

    def turnleft(self):
        self.head.left(90)
        self.feed(1) # Just to test
    def turnright(self):
        self.head.right(90)