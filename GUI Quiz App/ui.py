import time
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz APP")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 18, "bold"))
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="", width=290, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        correct_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=correct_image, highlightthickness=0, command=self.call_correct)
        self.correct_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.call_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """Gets next question, and set canvas text."""
        self.canvas.config(bg="white")
        # check if user reached end of the quiz
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of the quiz.....")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def call_false(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback_by_bg_color(is_false)

    def call_correct(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback_by_bg_color(is_true)

    def give_feedback_by_bg_color(self, is_correct):
        """Changes background color of canvas depending on user answer."""
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
