import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
car = CarManager()
car_iteration = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate car every 6 iterations
    if car_iteration == 0 or car_iteration == 6:
        car.generate_car()
        car.move_car()
        if car_iteration == 6:
            car_iteration = -1
    car_iteration += 1

    # Turtle hits top edge of the screen
    if player.ycor() >= 280:
        player.start_again()
        car.level_up()
        scoreboard.increase_level()

    # Turtle collides with car
    for item in car.car_lst:
        if item.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
