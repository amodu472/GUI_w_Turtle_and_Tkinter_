import turtle
from random import choice
from turtle import Turtle, Screen

# Change color mode since we're going to be using random rgb values for our colors
turtle.colormode(255)
# import colorgram
#
# color_amt = int(input("How many colors would you like? "))
# colors = colorgram.extract('image.jpg', color_amt)
# # List comprehension for extracting r,g,b values for the colors
# color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

color_list_ = [(234, 232, 227), (230, 233, 239), (239, 231, 235), (228, 235, 231), (199, 161, 100), (62, 91, 127),
               (139, 170, 191), (137, 90, 48), (219, 206, 119), (134, 27, 53), (32, 41, 67), (78, 17, 36),
               (150, 59, 86), (186, 141, 160), (166, 155, 49), (133, 183, 146), (46, 55, 102), (183, 94, 107),
               (57, 39, 27), (93, 117, 171), (64, 122, 107), (82, 149, 160), (91, 152, 93), (221, 175, 187),
               (163, 201, 214), (170, 205, 166), (192, 98, 74), (78, 71, 42), (182, 187, 210), (35, 56, 56),
               (224, 178, 171), (131, 39, 30)]

g = Turtle("turtle")


def create_dots():
    """This function creates dots using a nested loop"""
    g.hideturtle()
    g.penup()
    y_cor = -215
    for i in range(10):
        g.goto(-275, y_cor)
        y_cor += 50
        for j in range(10):
            g.fd(50)
            g.dot(20, choice(color_list_))


create_dots()

s = Screen()
s.mainloop()
