from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

def moveforward():
    pen.fd(10)    

def movebackward():
    pen.bk(10)

def moveleft():
    pen.left(10)

def moveright():
    pen.right(10)

def clear():
    pen.home()
    pen.clear()

screen.listen()

screen.onkey(clear, 'c') # Restart

screen.onkey(moveforward, 'w')
screen.onkey(movebackward, 's')
screen.onkey(moveleft, 'a')
screen.onkey(moveright, 'd') 

screen.exitonclick()