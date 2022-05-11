from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    text = list(item.values())[0]
    ans = list(item.values())[1]
    new_q = Question(text, ans)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was {quiz.score}/ {len(question_bank)}")
