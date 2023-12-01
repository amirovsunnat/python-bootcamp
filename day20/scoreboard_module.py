from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Monaco", 18, "bold")


class ScoreBoard(Turtle):
    """Scoreboard class inherits from Turtle."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_score(self):
        """Updates score."""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard."""
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Returns a message of game over, and user final score."""
        self.goto(0, 0)
        self.write(arg=f"Game Over. Your Final Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)




