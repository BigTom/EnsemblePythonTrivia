import unittest

from Trivia import Game

class RegressionTest(unittest.TestCase):

    def test_straight_unittest(self):
        game = Game(1)
        game.add('Chet')
        self.assertEqual(1, len(game.players))

    def test_question_shuffle(self):
        game = Game(42)
        game.shuffle_questions()
        self.assertEqual(42, len(game.pop_questions))
        self.assertEqual(42, len(game.rock_questions))
