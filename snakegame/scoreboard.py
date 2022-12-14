from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scorboard()

    def update_scorboard(self):
        self.write(f" score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f" Game over", align=ALIGN, font=FONT)
