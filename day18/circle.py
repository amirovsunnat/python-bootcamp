import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
drawer = Turtle()
drawer.speed(0)


def draw_spirograph(dis_bet_circle):
    for i in range(int(360 / dis_bet_circle)):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        drawer.color(color)
        drawer.circle(100)
        drawer.setheading(drawer.heading() + dis_bet_circle)


draw_spirograph(2)
screen.exitonclick()
