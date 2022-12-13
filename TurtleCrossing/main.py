import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    car.make_car()
    car.move()
    screen.update()

    for c in car.cars:
        if player.distance(c) < 21:
            level.game_over()
            game_is_on = False

    if player.finish_line():
        player.refresh_start()
        car.speed_up()
        level.increase_level()

screen.exitonclick()
