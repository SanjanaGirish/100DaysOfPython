from turtle import Turtle, Screen
from random import randint
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race? '
                                   'Enter a color: ')
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
for i in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.speed(7)
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won. The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")
        rand_dist = randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
