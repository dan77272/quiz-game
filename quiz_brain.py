class QuizBrain:
    def __init__(self, question_input):
        self.question_number = 0
        self.question_input = question_input
        self.score = 0
        self.total_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_input)

    def check_answer(self, useranswer, answer):
        if useranswer == answer:
            print("You got it right!")
            print(f"The correct answer was {useranswer}")
            self.score += 1
            self.total_score += 1
            print(f"Your current score is {self.score}/{self.total_score}")

        else:
            print("That's wrong")
            print(f"The correct answer was {answer}")
            self.total_score += 1
            print(f"Your current score is {self.score}/{self.total_score}")

    def next_question(self):
        current_question = self.question_input[self.question_number]
        self.question_number += 1
        useranswer = input(f"Q.{self.question_number} {current_question.text} (True/False)?: ")
        self.check_answer(useranswer, current_question.answer)
