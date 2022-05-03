import turtle as t
import random

tim = t.Turtle()
jes = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
jes.pensize(15)
jes.speed("fastest")

while True:
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    jes.color(random.choice(colours))
    jes.forward(30)
    jes.setheading(random.choice(directions))

# Turtle Sea!
# Fun idea, too lazy to make rn...