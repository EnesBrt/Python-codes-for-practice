from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = MOVE_INCREMENT

    def make_car(self):
        random_chance = random.randint(1, 6)
        self.hideturtle()
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-245, 245)
            new_car.goto(310, random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
