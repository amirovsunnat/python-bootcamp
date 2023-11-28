from turtle import Turtle, Screen


my_turtle = Turtle()
my_turtle.left(90)
my_turtle.forward(100)
for _ in range(3):
    my_turtle.right(90)
    my_turtle.forward(100)

screen = Screen()
screen.exitonclick()
