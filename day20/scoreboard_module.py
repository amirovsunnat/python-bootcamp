from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Monaco", 18, "bold")


class ScoreBoard(Turtle):
    """Scoreboard class inherits from Turtle."""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_score(self):
        """Updates score."""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard."""
        self.clear()
        self.write(arg=f"Score: {self.score}  Highest Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        """Resets score to initial value and updates high_score."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()



