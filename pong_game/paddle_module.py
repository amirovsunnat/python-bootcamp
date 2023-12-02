from turtle import Turtle


class Paddle(Turtle):
    """Paddle class."""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x_cor = position[0]
        self.goto(position)

    def move_up(self):
        """Move paddle to up by 40."""
        new_y = self.ycor() + 40
        self.goto(self.x_cor, new_y)

    def move_down(self):
        """Move paddle to down by 40."""
        new_y = self.ycor() - 40
        self.goto(self.x_cor, new_y)

