import turtle
from turtle import Turtle, Screen

import pandas

screen = Screen()
screen.setup(width=700, height=500)
screen.title("US States Naming Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States Correct.",
                                  prompt="What's another state name?").strip().title()
    if user_guess == "Exit":
        should_learn = [state for state in states if state not in guessed_states]  # use list comprehension
        pandas.DataFrame(should_learn).to_csv("should_learn_state.csv")
        break

    # check answer is in states
    if user_guess in states:
        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        state_info = data[data.state == user_guess]
        writer.goto(int(state_info.x), int(state_info.y))
        writer.write(arg=user_guess, align="center", font=("Courier", 11, "bold"))
        guessed_states.append(user_guess)

screen.mainloop()
