from turtle import Turtle


class Player(Turtle):
    """This class inherits from the turtle class and defines behaviours for a player trying to evade obstacles"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.seth(90)

    def move(self):
        self.fd(10)

    def reset_(self):
        self.goto(0, -280)
