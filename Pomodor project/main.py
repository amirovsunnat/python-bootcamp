import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = ""


# create reset timer function
def reset_timer():
    """Resets the timer."""
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    reps = 0


# create countdown function
def count_down(count):
    """Counts down count number."""
    global reps
    count_minutes = count // 60  # gives integer which is minutes
    count_seconds = count % 60  # gives remainder which is seconds
    if count_minutes < 10:
        count_minutes = f"{0}{count_minutes}"
    if count_seconds < 10:
        count_seconds = f"{0}{count_seconds}"
    canvas.itemconfig(time_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# create function to trigger count down function
def start_timer():
    """Triggers count down function."""
    global reps
    reps += 1
    working_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # display ticks
    ticks = [i for i in range(reps // 2)]
    tick_label.config(text=len(ticks)*"✔️")

    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 != 0:
        count_down(working_seconds)
        timer_label.config(text="Working Time", fg=GREEN)
    else:
        count_down(short_break_seconds)
        timer_label.config(text="Short Break", fg=PINK)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
pomodoro_image = PhotoImage(file="tomato.png")
# create image
canvas.create_image(100, 112, image=pomodoro_image)
# create text
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))

# create timer label
timer_label = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

# create start and reset buttons
start_bt = Button(text="Start", bg="white", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_bt.grid(column=0, row=3)

reset_bt = Button(text="Reset", bg="white", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
reset_bt.grid(column=2, row=3)

# create label tick
tick_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
tick_label.grid(column=1, row=4)

window.mainloop()
