class TriviaQuestions:
    def __init__(self, number_of_questions, question_label):
        self.question_label = question_label
        self.number_of_questions = number_of_questions
        self.shuffle_questions()

    def shuffle_questions(self):
        self.questions = []
        for i in range(self.number_of_questions):
            self.questions.append("%s Question %s" % (self.question_label, i))
