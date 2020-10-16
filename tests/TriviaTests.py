import unittest

from Trivia import Game

class RegressionTest(unittest.TestCase):

    def test_straight_unittest(self):
        game = Game(1)
        game.add('Chet')
        self.assertEqual(1, len(game.players))