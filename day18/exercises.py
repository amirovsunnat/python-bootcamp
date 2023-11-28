import random
from turtle import Turtle, Screen

# # draw a square
# my_turtle = Turtle()
# my_turtle.left(90)
# my_turtle.forward(100)
# for _ in range(3):
#     my_turtle.right(90)
#     my_turtle.forward(100)


# # draw dashed line
# john = Turtle()
# for _ in range(15):
#     john.forward(10)
#     john.penup()
#     john.forward(10)
#     john.pendown()


# # draw different shapes
# colors = ["red", "yellow", "orange", "blue", "grey", "purple"]
#
#
# def draw_shapes(number_sides):
#     """Takes numbers of sides and draws shapes."""
#     side_len = 100
#     drawer = Turtle()
#     for i in range(3, number_sides):
#         drawer.color(random.choice(colors))
#         angel = 360 / i
#         for j in range(i):
#             drawer.forward(side_len)
#             drawer.right(-angel)
#
#
# draw_shapes(50)


# random walk
colors = ["red", "yellow", "orange", "blue", "grey", "purple"]
angels = [90, 180, 270]
walker = Turtle()
walker.width(5)
walker.turtlesize(2, 3, 2)
while True:
    walker.forward(10)
    walker.color(random.choice(colors))
    walker.setheading(random.choice(angels))

screen = Screen()
screen.exitonclick()


