from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 55, "bold")


class ScoreBoard(Turtle):
    """ScoreBoard class."""
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 220)
        self.update_scoreboard()

    def increase_left_score(self):
        """Increases left score."""
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        """Increases right score."""
        self.right_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.left_score}   {self.right_score}", align=ALIGNMENT, font=FONT)
