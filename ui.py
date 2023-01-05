from tkinter import Tk, Label, Canvas, Button, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#ffffff"
GREEN = "#45eb42"
RED = "#ff1212"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score_display = Label(text="Score:0/10", bg=THEME_COLOR, font=("Arial", 15))
        self.question_box = Canvas(height=250, width=300, bg=WHITE)
        self.question_text = self.question_box.create_text(
            150,
            125,
            text=" ",
            font=("Arial", 20, "italic"),
            width=280
        )
        # self.question_text = self.question_box.create_text(
        #     150,
        #     125,
        #     text=" ",
        #     font=("Arial", 11, "italic"),
        #     width=280
        # )
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, command=self.true_func)
        self.false_button = Button(image=self.false_image, command=self.false_func)
        self.score_display.grid(row=0, column=1, pady=20)
        self.question_box.grid(row=1, column=0, padx=20, pady=20, columnspan=2)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_button.grid(row=2, column=1, pady=20)
        self.get_next_question()
        self.window.mainloop()
    
    def button_pass(self):
        pass

    def button_enable(self):
        self.true_button.configure(command=self.true_func)
        self.false_button.configure(command=self.false_func)

    def true_func(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_func(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def get_next_question(self):
        qtext = self.quiz.next_question()
        self.question_box.itemconfig(self.question_text, text=qtext)
        self.score_display.configure(text=f"Score:{self.quiz.score}/10")

    def give_feedback(self, is_right: bool):
        self.true_button.configure(command=self.button_pass)
        self.false_button.configure(command=self.button_pass)
        if is_right is True:
            self.question_box.configure(bg=GREEN)
        elif is_right is False:
            self.question_box.configure(bg=RED)
        self.question_box.after(1300, self.reset_box)

    def reset_box(self):
        self.question_box.configure(bg=WHITE)
        if self.quiz.question_number < 10:
            self.get_next_question()
            self.button_enable()
        elif self.quiz.question_number >= 10:
            self.question_box.itemconfig(self.question_text, text="Game Over")
