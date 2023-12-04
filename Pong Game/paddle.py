import turtle
from turtle import Turtle
turtle.mode("logo")


class Paddle(Turtle):
    """This class inherits from Turtle to initialize a paddle and define methods for interacting with it"""
    def __init__(self, position):
        super().__init__()
        # paddle setup
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)

    # functions for responding to keystrokes
    def up(self):
        if self.ycor() < 250:
            self.seth(0)
            self.fd(20)

    def down(self):
        if self.ycor() > -250:
            self.seth(180)
            self.fd(20)
