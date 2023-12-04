from turtle import Turtle, Screen
from random import randint

# Screen setup
s = Screen()
s.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_axis = 160
racers = []

# Turtles instantiating
for i in range(len(colors)):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-235, y_axis)
    y_axis -= 60
    racers.append(tim)

# Prompt user to make a bet (I DO NOT condone gambling whatsoever!!!)
user_bet = s.textinput(title="Place your bet...", prompt="What color are you betting on? ").lower()

# Game continues till there is a winner
game_not_over = True
while game_not_over:
    for racer in racers:
        racer.fd(randint(1, 10))
        if racer.xcor() > 220:
            if racer.pencolor() == user_bet:
                print("You bet correctly! Here's your $1m!")
            else:
                print("Wrong bet! Better luck next time!")
            game_not_over = False

s.mainloop()
