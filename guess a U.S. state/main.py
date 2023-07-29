import turtle
from turtle import Screen, Turtle
from turtle import *
import pandas as pd

screen = Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f" {len(guess_states)} / 50 correct states", prompt="What is the stats names ?").title()
    if answer_state == "Exit":
        missing_states = [n for n in all_states if n not in guess_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        df_state = df[df["state"] == answer_state]
        t.goto(int(df_state.x), int(df_state.y))
        t.write(answer_state)

screen.exitonclick()