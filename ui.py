from tkinter import Tk, Label, Canvas, Button, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
def button_filler():
    pass

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score_display = Label(text="Score:0", bg=THEME_COLOR)
        self.question_box = Canvas(height=250, width=300)
        self.question_text = self.question_box.create_text(
            150,
            125,
            text="Test",
            font=("Arial", 20, "italic")
        )
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, command=button_filler)
        self.false_button = Button(image=self.false_image, command=button_filler)
        self.score_display.grid(row=0, column=1, pady=20)
        self.question_box.grid(row=1, column=0, padx=20, pady=20, columnspan=2)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_button.grid(row=2, column=1, pady=20)
        self.get_next_question()
        # Why is this not working?
        self.window.mainloop()

    def get_next_question(self):
        qtext = self.quiz.next_question()
        self.question_box.itemconfig(self.question_text, text=qtext)
