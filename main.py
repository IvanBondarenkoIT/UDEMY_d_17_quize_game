from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

q_b = QuizBrain(question_bank)
q_b.next_question()

while q_b.still_has_questions():
    q_b.next_question()

print("You've completed the quiz")
print(f"Your final score was: {q_b.score}/{q_b.question_number}")