from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Creating score label
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, highlightthickness=0,
                           font=("Arial", 15, "bold"))
        self.score.grid(column=1, row=0)

        # Creating tick and x button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        # Creating canvas with the question
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(tagOrId=self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(tagOrId=self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="GreenYellow")
        else:
            self.canvas.config(bg="Salmon")
        self.window.after(ms=1000, func=self.get_next_question)
