import random
from turtle import Turtle


class Ball(Turtle):
    """Ball class."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.1

    def move(self):
        """Moves ball continuously."""
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x=x_pos, y=y_pos)

    def bounce_y(self):
        """Reverse ycor when collision happens."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse xcor when collision happens."""
        self.x_move *= -1
        self.moving_speed *= 0.9

    def reset_position(self):
        """Resets ball position. Reverse xcore direction."""
        self.goto(0, 0)
        self.bounce_x()
        self.moving_speed = 0.1



