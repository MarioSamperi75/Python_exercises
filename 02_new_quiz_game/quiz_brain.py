class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def still_has_questions(self):
        #if self.question_number < len(self.question_list):
        #    return True
        #return False
        return self.question_number < len(self.question_list)

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {item.text} (true/false):")
        self.check_answer(user_answer, item.answer)
        return item

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was {answer}.")
        print(f"Your current score is: {self.score}/{self.question_number} \n\n")
