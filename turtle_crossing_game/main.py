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
score = Scoreboard()

screen.listen()
screen.onkey(player1.move, "Up")

game_is_on = True
loop_count = 0
# run_time = 0.1
while game_is_on:
    loop_count += 1
    time.sleep(0.1)
    screen.update()

    # level_up if player reaches the endline
    if player1.ycor() >= 290:
        player1.finish()
        score.level_up()
        cars.increase_speed()
        # run_time *= 0.9

    #create and move cars
    cars.move1()
    if loop_count % 6 == 0 or loop_count == 1:
        cars.create_car()

    # detect collision with the car
    for x in cars.all_cars:
        if player1.distance(x) < 25:
            score.game_over()
            game_is_on = False


screen.mainloop()
