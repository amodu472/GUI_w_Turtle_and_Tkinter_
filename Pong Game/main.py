import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# Initialize paddles, ball and scores
ball = Ball()
l_paddle = Paddle((-375, 0))
r_paddle = Paddle((375, 0))
l_score = ScoreBoard((-50, 250))
r_score = ScoreBoard((50, 250))


# Listen for keystrokes
screen.listen()
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="z", fun=l_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

# Keep playing game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.paddle_bounce()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()
    elif ball.xcor() > 390:
        ball.reset_()
        l_score.update_score()
    elif ball.xcor() < -390:
        ball.reset_()
        r_score.update_score()

screen.mainloop()
