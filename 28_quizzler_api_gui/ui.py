from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
dummy_text = "Questa affermazione corrisponde a verità"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="#ffffff")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="#ffffff")
        self.question_text = self.canvas.create_text(150, 125, text=dummy_text, width=270, fill=THEME_COLOR, font=("Arial", 14, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # self.question_label = Label(height=250, width=300, padx=20, font=("Arial", 20, "italic"), text=dummy_text)
        # self.question_label.grid(row=1, column=0)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.on_true_click)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.on_false_click)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def on_true_click(self):
        self.quiz.check_answer("True")

    def on_false_click(self):
        self.quiz.check_answer("False")
