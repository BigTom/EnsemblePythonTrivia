import unittest
from trivia_questions import TriviaQuestions

class Test_Trivia_Questions(unittest.TestCase):
    def test_initial_class(self):
        questions = TriviaQuestions(42, 'Pop')
        self.assertEqual(42, len(questions.questions))
        self.assertEqual('Pop Question 0', questions.questions[0])
