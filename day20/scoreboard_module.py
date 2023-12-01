from turtle import Turtle


class ScoreBoard(Turtle):
    """Scoreboard class inherits from Turtle."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """Updates score."""
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="Center", font=("Monaco", 18, "bold"))
        self.score += 1




