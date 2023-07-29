from turtle import Screen
from paddle import Paddle
from ball import Ball
from target import Target
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=400, height=800)
screen.title("Touch target")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
target = Target()
score = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    if ball.xcor() > 180 or ball.xcor() < -180:
        ball.bounce_x()

    if ball.distance(paddle) < 40 and ball.ycor() < -320:
        ball.bounce_y()

    if ball.distance(target) < 40 and ball.ycor() > 320:
        ball.bounce_y()
        score.score_up()
        ball.speed_up()

    if ball.ycor() > 360:
        ball.bounce_y()

    if ball.ycor() > 400:
        score.game_over()
        game_is_on = False


screen.exitonclick()
