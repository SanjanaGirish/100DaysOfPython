class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        ask_q = input(f"Q.{self.question_number} {current_q.text} "
                      f"(True/False)")
        self.check_answer(ask_q, current_q.answer)

    def still_has_questions(self):
        return self.question_number < 12

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was:{correct_ans}")
        print(f"Your current score is {self.score}/ {self.question_number}")
        print("\n")
