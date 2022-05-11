from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_lst = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle("square")
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        rand_y = randint(-250, 250)
        new_car.goto(280, rand_y)
        self.car_lst.append(new_car)

    def move_car(self):
        for car in self.car_lst:
            car.backward(MOVE_INCREMENT)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
