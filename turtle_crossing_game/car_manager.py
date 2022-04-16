from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randint(-220, 220))
        self.forward(STARTING_MOVE_DISTANCE)

    def move1(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())