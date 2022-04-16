import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player1 = Player()
cars = CarManager()

screen.listen()
screen.onkey(player1.move, "Up")

game_is_on = True
loop_count = 0
while game_is_on:
    loop_count += 1
    time.sleep(0.1)
    screen.update()

    cars.move1()
    if loop_count % 6 == 0 or loop_count == 1:
        cars.create_car()



