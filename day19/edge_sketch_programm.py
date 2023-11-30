from turtle_race_game import Turtle, Screen


jim = Turtle()
screen = Screen()


def move_forward():
    """Moves turtle forward to up 10 space."""
    jim.forward(10)


def move_back():
    """Moves turtle back to down 10 space."""
    jim.back(10)


def turn_right():
    """Turns turtle to right 10 angle."""
    jim.setheading(jim.heading() - 10)


def turn_left():
    """Turns turtle to left 10 angle."""
    jim.setheading(jim.heading() + 10)


def clear_screen():
    """Clears screen."""
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
