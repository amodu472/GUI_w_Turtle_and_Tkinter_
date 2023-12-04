from turtle import Turtle
from random import randint
import turtle

turtle.colormode(255)


# rgb color values
def r_g_b():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return r, g, b


class Car:
    """This class models a car (obstacle) to be avoided by the player"""
    def __init__(self):
        self._MOVE_INCREMENT = 5
        self.cars = []

    def generate_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(r_g_b())
        random_y = randint(-250, 250)
        new_car.goto(310, random_y)
        new_car.seth(180)

        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.fd(self._MOVE_INCREMENT)

    def next_level(self):
        self._MOVE_INCREMENT += 5
