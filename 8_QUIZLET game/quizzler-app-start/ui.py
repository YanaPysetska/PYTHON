from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.my_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 10))
        self.my_label.grid(column=1, row=0)

        my_image_false = PhotoImage(file="images/false.png")
        my_image_true = PhotoImage(file="images/true.png")

        # Add command to buttons
        self.button_false = Button(image=my_image_false, bd=0, highlightthickness=0, command=self.false_answer)
        self.button_false.grid(column=1, row=2)
        self.button_true = Button(image=my_image_true, bd=0, highlightthickness=0, command=self.true_answer)
        self.button_true.grid(column=0, row=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Quote goes here", width=280, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.my_label.config(text=f"Score {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
