import turtle as t
import random

go = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def dots(space, x):
    for i in range(x):
        for j in range(x):
            go.speed("fastest")
            go.dot(20, random_color())
            go.forward(50)

        go.backward(space * x)

        # direction
        go.right(90)
        go.forward(space)
        go.left(90)


go.penup()
dots(50, 10)

go.hideturtle()
screen = t.Screen()
t.exitonclick()
