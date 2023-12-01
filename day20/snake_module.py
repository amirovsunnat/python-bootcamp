from turtle import Turtle


class Snake:
    """Snake class."""
    def __init__(self):
        self.turtles = []
        self.x_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        """Create snake when snake class is initialized"""
        # create turtle object
        for position in self.x_pos:
            self.add_snake_part(position)

    def move(self):
        """Move snake."""
        for t in range(len(self.turtles) - 1, 0, -1):
            x_coordinate = self.turtles[t - 1].xcor()
            y_coordinate = self.turtles[t - 1].ycor()
            self.turtles[t].goto(x_coordinate, y_coordinate)
        self.head.forward(10)

    def add_snake_part(self, position):
        """Creates new part of snake"""
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.shapesize(stretch_len=0.5, stretch_wid=0.5)
        snake.speed("fastest")
        snake.goto(position)
        self.turtles.append(snake)

    def extend_snake(self):
        """Add new part to snake."""
        self.add_snake_part(self.turtles[-1].position())

    def up(self):
        """Moves snake to up."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Moves snake to down."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Turns snake to left."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Turns snake to right."""
        if self.head.heading() != 180:
            self.head.setheading(0)
