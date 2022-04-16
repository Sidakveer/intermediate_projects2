from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []


    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(300, random.randint(-220, 220))
        new_car.forward(STARTING_MOVE_DISTANCE)
        self.all_cars.append(new_car)

    def move1(self):
        for x in self.all_cars:
            x.forward(STARTING_MOVE_DISTANCE)
