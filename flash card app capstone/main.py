from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# create canvas front image
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
# create canvas background image
card_background_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_background_image)
# create text
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create image and put it to buttons
x_image = PhotoImage(file="images/wrong.png")
true_image = PhotoImage(file="images/right.png")
right_button = Button(image=true_image, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button = Button(image=x_image, highlightthickness=0)
wrong_button.grid(row=1, column=1)


window.mainloop()
