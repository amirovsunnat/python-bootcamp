class QuizBrain:
    """QuizBrain class"""
    def __init__(self, questions_list):
        self.question_number = 0
        self._score = 0
        self.questions_list = questions_list

    def still_has_question(self):
        """Returns true if question list has element, otherwise false."""
        return len(self.questions_list) > self.question_number

    def next_question(self):
        """Ask question, and returns next question."""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        # asks a question
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").strip().title()
        self.check_answer(user_answer=user_answer, correct_answer=current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks entered answer, then returns message regarding answer."""
        if user_answer == correct_answer:
            print("You got it right!")
            self._score += 1
        else:
            print("You got it wrong. SORRY.....")
        print(f"The correct answer was: {correct_answer}")
        print(f"The current score is: {self._score}/{self.question_number}")

    @property
    def score(self):
        return self._score
