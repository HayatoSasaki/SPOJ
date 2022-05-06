from turtle import Turtle

# Directions.
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

# Create the Snake.
    def __init__(self):
        self.head = Turtle(shape='square')
        self.head.color('white')
        self.head.penup()
        self.tail = []
        self.feed(2)        
        
        for _ in range(2):
            self.tail[_].goto((self.head.xcor()-20*(_+1), self.head.ycor()))

# Feed the Snake.
    def feed(self, food):
        for _ in range(food):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            if len(self.tail) < 1:
                new_segment.goto(self.head.xcor(), self.head.ycor)
            else:
                new_segment.goto((self.tail[-1].xcor(), self.tail[-1].ycor()))
            self.tail.append(new_segment)

# Move the Snake.
    def move(self, steps):
        new_movement = [self.head.xcor(), self.head.ycor()]
        self.head.forward(steps) # Movement.
        for segment in self.tail:
            old_movement = [segment.xcor(), segment.ycor()]
            segment.goto(new_movement)
            new_movement = old_movement

# Dead Snake and Ouroboros Snake.
    def dead(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
    def ouroboros(self):
        for _ in self.tail[1:]:
            if _.distance(self.head) < 15:
                return True

# Control the Snake.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)