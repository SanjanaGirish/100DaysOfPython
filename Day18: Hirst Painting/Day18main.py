from turtle import Turtle, Screen
from random import random, choice

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")

# task 1: turtle draws a square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# Task 2: turtle draws a dotted line
# for j in range(5):
#     for i in range(1):
#         timmy_the_turtle.down()
#         timmy_the_turtle.forward(10)
#     timmy_the_turtle.up()
#     timmy_the_turtle.forward(10)

# Task 3: Turtle draws all shapes from triange to decagon in diff colours
# def change_color():
#     R = random()
#     B = random()
#     G = random()
#     timmy_the_turtle.color(R, G, B)
# for i in range(3, 11):
#     for j in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360 / i)
#     change_color()

# Task 4: Random Walk in Turtle
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
#            "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# angles = [90, 180, 270, 360]
# timmy_the_turtle.speed(8)
# timmy_the_turtle.width(8)
# def walk():
#     timmy_the_turtle.color(choice(colours))
#     timmy_the_turtle.setheading(choice(angles))
#     timmy_the_turtle.forward(50)
# for i in range(50):
#     walk()

# Task 5: Creating a spirograph


def change_color():
    R = random()
    B = random()
    G = random()
    timmy_the_turtle.color(R, G, B)


timmy_the_turtle.speed(0)
for i in range(360 // 5):
    change_color()
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(5)

screen = Screen()
screen.exitonclick()
