import unittest

from Trivia import Game


class RegressionTest(unittest.TestCase):

    def test_confirm_number_of_players(self):
        game = Game()
        game.add('Chet')
        self.assertEqual(1, len(game.players))

    def test_number_of_questions_per_category(self):
        game = Game(42)
        game.shuffle_questions()
        self.assertEqual(42, len(game.pop_questions))
        self.assertEqual(42, len(game.rock_questions))
        self.assertEqual(42, len(game.science_questions))
        self.assertEqual(42, len(game.sports_questions))

    def test_asking_pop_question_decreases_question_list(self):
        game = Game(2)
        game.add('Chet')  # rename to addPlayer?
        game.shuffle_questions()
        pop_location = 0
        game.roll(pop_location)
        self.assertEqual(1, len(game.pop_questions), "Pop")

    def test_asking_science_question_decreases_question_list(self):
        game = Game(2)
        game.add('Chet')  # rename to addPlayer?
        game.shuffle_questions()
        science_location = 1
        game.roll(science_location)
        self.assertEqual(1, len(game.science_questions), "Science")

    def test_asking_sports_question_decreases_question_list(self):
        game = Game(2)
        game.add('Chet')  # rename to addPlayer?
        game.shuffle_questions()
        sports_location = 2
        game.roll(sports_location)
        self.assertEqual(1, len(game.sports_questions), "Sports")

    def test_asking_rock_question_decreases_question_list(self):
        game = Game(2)
        game.add('Chet')  # rename to addPlayer?
        game.shuffle_questions()
        rock_location = 3
        game.roll(rock_location)
        self.assertEqual(1, len(game.rock_questions), "Rock")

    def test_asking_more_questions_than_are_in_category_resets_the_questions_in_that_category(self):
        game = Game(2)
        game.add('Chet')  # rename to addPlayer?
        game.shuffle_questions()
        science_location = 1
        game.roll(science_location)
        number_of_categories = 4
        game.roll(number_of_categories)
        self.assertEqual(0, len(game.science_questions), "Science")

        game.roll(number_of_categories)
        self.assertEqual(1, len(game.science_questions), "Science")
