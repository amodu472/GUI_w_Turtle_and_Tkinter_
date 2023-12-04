from turtle import Turtle
from random import randint


class Food(Turtle):
    """This class inherits from Turtle. It 'transforms' some of its attributes to simulate in-game food."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(randint(-275, 275), randint(-275, 275))
