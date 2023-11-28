# import colorgram
# colors = []
# # Extract 15 colors from an image.
# colors_from_painting = colorgram.extract('hirst_spots_painting.jpg', 15)
# for color in colors_from_painting:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors.append((r, g, b))
import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.speed(0)
timmy.penup()
# deleted whitish colors
colors = [(249, 228, 18), (212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188), (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48)]
timmy.goto(-250, -200)
number_of_dots = 100
for dots in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)

    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

timmy.hideturtle()

screen.exitonclick()
