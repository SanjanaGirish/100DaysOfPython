from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas - Quiz Questions
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Text on Canvas
        self.question_text = self.canvas.create_text(150, 125, text="Question",
                                font=("Arial", 20, "italic"), fill=THEME_COLOR,
                                                     width=280)
        # Correct-Button (✅)
        right_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=right_image, highlightthickness=0,
                                   command=self.guessing_correct)
        self.right_button.grid(row=2, column=0)

        # Wrong-button (❌)
        wrong_image = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=wrong_image, highlightthickness=0,
                                   command=self.guessing_wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=ques_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="You have reached the end of the Quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def guessing_correct(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def guessing_wrong(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

