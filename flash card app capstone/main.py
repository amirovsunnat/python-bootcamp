import random
from tkinter import *
import pandas

current_card = {}
words_list = {}


try:
    data = pandas.read_csv("data/word_need_to_learn.csv")
except FileNotFoundError:
    original_word = pandas.read_csv("data/french_words.csv")
    words_list = original_word.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


def next_card():
    """Returns random word."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flips card."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_background_image)


def is_known_word():
    """Checks and reduce word list, save them into csv and go to next word."""
    word_list.remove(current_card)
    new_data = pandas.DataFrame(word_list)
    new_data.to_csv("data/word_need_to_learn.csv", index=False)
    next_card()


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# create canvas front image
card_front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
# create canvas background image
card_background_image = PhotoImage(file="images/card_back.png")
# create text
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create image and put it to buttons
x_image = PhotoImage(file="images/wrong.png")
true_image = PhotoImage(file="images/right.png")
right_button = Button(image=true_image, highlightthickness=0, command=is_known_word)
right_button.grid(row=1, column=1)
wrong_button = Button(image=x_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# in order to show title and word on the canvas we need to call next card function
next_card()

window.mainloop()
