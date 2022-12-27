from tkinter import Tk,Label,Canvas

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score_display = Label(text="Score:0", width=300, height=300, padx=20)
        self.question_box = Canvas()
        self.question_text = self.question_box.create_text(
            0,
            0,
            text="Test",
            font=("Arial", 20, "italic")
        )
        self.question_box.config(height=250, width=300, padx=20)
        self.score_display.grid(row=0, column=1)
        self.question_box.grid(row=1, column=0)
        self.window.mainloop()
