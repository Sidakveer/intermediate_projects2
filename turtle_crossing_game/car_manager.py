from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 100


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(300, random.randint(-220, 220))
        self.all_cars.append(new_car)

    def move1(self):
        for x in self.all_cars:
            x.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
