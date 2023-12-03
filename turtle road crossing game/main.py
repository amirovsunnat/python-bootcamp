import time
from turtle import Screen

from player_module import Player
from car_module import Car
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Road Crossing Game")
screen.tracer(0)

# create player object
player = Player()

# create car object
car = Car()

# create scoreboard object
scoreboard = ScoreBoard()


# start listening keystrokes
screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # detect collision with cars
    for c in car.all_cars:
        if player.distance(c) < 20:
            game_on = False
            scoreboard.game_over()

    # check player come to finish line, then reset position
    if player.is_player_in_finish():
        player.return_to_start()
        # increase car speed
        car.speed_up()
        # update scoreboard
        scoreboard.increase_level()

screen.exitonclick()
