from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.goto(-240, 240)
        self.scores()

    def scores(self):
        self.write(f"Level :  {self.score}", move=False, align="center", font=("Arial", 18, "normal"))

    def score_increase(self):
        self.clear()
        self.score += 1
        self.scores()

    def game_over(self):
        self.clear()
        self.color("black")
        self.goto(0, 0)
        self.write(f"     Game over\n Your score is :  {self.score}", move=False, align="center",
                   font=("Arial", 22, "bold"))
