import random
from turtle import Turtle


class Food(Turtle):
    """Food class inherits from Turtle."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.move_another_place()

    def move_another_place(self):
        """Moves food to another random place."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
