import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect when turtle collides with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False

    # detect if turtle reaches the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

scoreboard.game_over()

screen.exitonclick()
