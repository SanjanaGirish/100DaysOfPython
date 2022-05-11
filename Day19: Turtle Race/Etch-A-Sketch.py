from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(-10)


def clear1():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
# we don't add the parenthesis when we are calling a function
# inside another function
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clockwise, "a")
screen.onkey(counter_clockwise, "d")
screen.onkey(clear1, "c")
screen.exitonclick()
