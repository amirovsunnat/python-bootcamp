import time
from turtle import Turtle, Screen

from paddle_module import Paddle
from ball_module import Ball
from scoreboard_module import ScoreBoard


screen = Screen()
screen.title("Pong Game Of Sunnat")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# create left and right paddles
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

# create ball
ball = Ball()

# create scoreboard
scoreboard = ScoreBoard()

# start listening on keyboards
screen.listen()

# movement of right paddle
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

# movement of left paddle
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

game_on = True
while game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()
    # detect collision with top and bottom
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with right and left paddle
    if ((ball.distance(r_paddle) < 30 and ball.xcor()) > 330
            or (ball.distance(l_paddle) < 30 and ball.xcor() < -330)):
        ball.bounce_x()

    # detect when right paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()

    # detect when left paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()

screen.exitonclick()
