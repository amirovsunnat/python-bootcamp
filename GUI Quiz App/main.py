import requests

from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
parameters = {
    "amount": 10,
    "type": "boolean"
}


def get_questions():
    """Gets questions from API, and returns them."""
    url = "https://opentdb.com/api.php"
    response = requests.get(url=url, params=parameters)
    # raise an exception if any error happens
    response.raise_for_status()
    data = response.json()
    global question_data
    question_data = data["results"]
    return question_data


question_data = get_questions()

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

# create quiz interface object
quiz_interface = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
