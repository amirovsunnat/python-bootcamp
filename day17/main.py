from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from logo import logo


questions_bank = []
for i in range(len(question_data)):
    question_text = question_data[i]["text"]
    question_answer = question_data[i]["answer"]
    question = Question(text=question_text, answer=question_answer)
    questions_bank.append(question)

quiz = QuizBrain(questions_list=questions_bank)
while quiz.still_has_question():
    print(logo)
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score: {quiz.score}/{len(questions_bank)}")



