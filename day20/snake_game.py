import time
from turtle import Screen

from day20.scoreboard_module import ScoreBoard
from day20.snake_module import Snake
from day20.food_module import Food

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# create snake object
snake = Snake()

# create food object
food = Food()

# create scoreboard object
scoreboard = ScoreBoard()

# start listening keyboard
screen.listen()

# set up keystrokes
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.move_another_place()
        snake.extend_snake()
        scoreboard.update_score()

    # detecting collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset()

    # detecting collision with snake body
    for part in snake.turtles[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset_score()
            snake.reset()


screen.exitonclick()
