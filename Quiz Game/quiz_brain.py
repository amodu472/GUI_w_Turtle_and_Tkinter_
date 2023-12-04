class QuizBrain:
    """This class is responsible for producing the next question, checking if the correct answer was entered
    and scoring the player."""

    def __init__(self, q_list):
        self._score = 0
        self._question_num = 0
        self._question_list = q_list
        self._total_questions = len(self._question_list)

    def next_question(self):
        """Produces the next question and checks if the correct answer was provided"""
        current_question = self._question_list[self._question_num]
        self._question_num += 1
        user_answer = input(f"Q.{self._question_num}: {current_question.text} True or False?: ").lower()
        return self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self._score += 1
        else:
            print(f"You got it wrong. The correct answer is {correct_answer}.")
        print(f"Your current score is {self._score}/{self._question_num}.")
        return "\n"

    def still_has_questions(self):
        return self._question_num < self._total_questions

    @property
    def score(self):
        return self._score

    @property
    def total_questions(self):
        return self._total_questions

    @property
    def question_num(self):
        return self._question_num
