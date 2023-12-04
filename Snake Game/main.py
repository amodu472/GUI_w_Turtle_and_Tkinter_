from score_board import ScoreBoard
from turtle import Screen
from snake import Snake
from food import Food
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Pause the animation with the tracer method as follows
screen.tracer(0)

# Initialize a snake object, then get screen to listen for commands
snake = Snake()
food = Food()
score = ScoreBoard()

# Get screen to listen and respond to key presses for snake control
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Game is going on. Animation is updated & segs are moving as follows:
game_is_on = True
while game_is_on:
    # Update the screen and sleep time after each 'movement' below
    screen.update()
    time.sleep(0.1)

    # get the snake to move
    snake.move()

    # Check for food collision
    if snake.head.distance(food) < 15:
        snake.extend()
        score.update()
        score.write_score()
        food.refresh()

    # check for wall collision
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 285:
        score.set_scores()
        score.write_score()
        snake.reset_()
    elif snake.tail_collision():
        score.set_scores()
        score.write_score()
        snake.reset_()

screen.mainloop()
