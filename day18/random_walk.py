import random
from turtle import Turtle, Screen


screen = Screen()
screen.colormode(255)


angels = [0, 90, 180, 270]

walker = Turtle()
walker.width(6)
walker.speed(0)
while True:
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    walker.forward(14)
    walker.color(color)
    walker.setheading(random.choice(angels))
