from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")


