from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.goto(-120, 350)
        self.write(f"score : {self.score}", align="center", font=("Courier", 15, "normal"))

    def score_up(self):
        self.score += 3
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.color("red")
        self.write(f" Game over", align="center", font=("Courier", 20, "normal"))

