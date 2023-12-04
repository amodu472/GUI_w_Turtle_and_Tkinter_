from scoreboard import ScoreBoard
from turtle import Screen
from player import Player
from car import Car
import time

# screen and animation setup
screen = Screen()
screen.title("Turtle Crossing")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

# Get the screen to listen for key presses
screen.listen()

# create player
player = Player()
car = Car()
score = ScoreBoard()

# Game loop and loop counter for generating new cars
game_on = True
loop_counter = 0

while game_on:
    # Update screen every .1 secs
    screen.update()
    time.sleep(0.1)
    loop_counter += 1

    # Gen new car every 8th time game loop runs
    if loop_counter % 8 == 0:
        car.generate_car()

    # check for collision
    for car_ in car.cars:
        if player.distance(car_) < 25:
            score.game_over()
            game_on = False

    # increment level and difficulty
    if player.ycor() > 285:
        player.reset_()
        car.next_level()
        score.level_up()

    car.move()
    # screen responds to key presses on screen
    screen.onkey(fun=player.move, key="Up")


screen.mainloop()
