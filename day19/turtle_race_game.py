import random
from turtle import Turtle, Screen

game_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_guess = screen.textinput(title="Guess a Color.", prompt="Which color of turtle will win? Make a guess: ")
colors = ["red", "blue", "green", "orange", "yellow", "cyan"]
turtles = []

y_pos = -150
for i in range(6):
    jimmy = Turtle("turtle")
    jimmy.color(colors[i])
    jimmy.penup()
    jimmy.goto(x=-270, y=y_pos)
    y_pos += 60
    turtles.append(jimmy)

if user_guess:
    game_on = True


while game_on:
    for each_turtle in turtles:
        if each_turtle.xcor() >= 280:
            game_on = False
            if user_guess == each_turtle.pencolor():
                print(f"You win! The winner color of turtle is {user_guess}")
            else:
                print(f"You lost. The winner color of turtle is {each_turtle.pencolor()}")
        random_distance = random.randint(0, 10)
        each_turtle.forward(random_distance)


screen.exitonclick()
