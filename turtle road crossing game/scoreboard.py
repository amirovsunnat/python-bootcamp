from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 25, "bold")


class ScoreBoard(Turtle):
    """ScoreBoard class."""
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-300, 240)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates scoreboard."""
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER. FINAL SCORE: {self.level}", align=ALIGNMENT, font=FONT)
