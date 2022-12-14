from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["blue", "red", "green", "orange", "indigo", "gold"]
y_axe = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axe[turtle])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won ! the {winning_color} turtle is the winner !")
            else:
                print(f"you've lost ! the {winning_color} turtle is the winner !")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
