from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVING_DISTANCE = 10
FINISHING_LINE = 300


class Player(Turtle):
    """Player class."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.return_to_start()
        self.setheading(90)

    def move_up(self):
        """Moves player up to 10 space."""
        self.forward(MOVING_DISTANCE)

    def move_down(self):
        """Moves player down to 10 space."""
        self.back(MOVING_DISTANCE)

    def return_to_start(self):
        """Return player to starting point."""
        self.goto(STARTING_POSITION)

    def is_player_in_finish(self):
        """Returns true if player is at finish line, otherwise false."""
        return self.ycor() >= FINISHING_LINE


