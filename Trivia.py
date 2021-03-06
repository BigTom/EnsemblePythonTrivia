#!/usr/bin/env python3
from trivia_questions import TriviaQuestions

MAX_PLAYERS = 6


class Game:
    def __init__(self, number_of_questions=50):
        self.players = []
        self.places = [0] * MAX_PLAYERS
        self.purses = [0] * MAX_PLAYERS
        self.in_penalty_box = [0] * MAX_PLAYERS

        self.pop_questions = TriviaQuestions(number_of_questions, 'Pop').questions
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.number_of_questions_in_category = number_of_questions

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(number_of_questions):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def shuffle_questions(self):
        self.populate_list("Pop", self.pop_questions)
        self.rock_questions = []
        self.shuffle_pop_questions()
        self.shuffle_rock_questions()

    def shuffle_pop_questions(self):
        self.pop_questions = []
        self.populate_list("Pop", self.pop_questions)

    def shuffle_rock_questions(self):
        self.rock_questions = []
        for i in range(self.number_of_questions_in_category):
            self.rock_questions.append("Rock Question %s" % i)
    #
    # def create_rock_question(self, index):
    #     return "Rock Question %s" % index

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            self.player_in_penalty_box(roll)
        else:
            self.player_not_in_penalty_box(roll)

    def player_not_in_penalty_box(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12
        print(self.players[self.current_player] + \
              '\'s new location is ' + \
              str(self.places[self.current_player]))
        print("The category is %s" % self._current_category)
        self._ask_question()

    def player_in_penalty_box(self, roll):
        if roll % 2 != 0:
            self.is_getting_out_of_penalty_box = True

            print("%s is getting out of the penalty box" % self.players[self.current_player])
            self.player_not_in_penalty_box(roll)
        else:
            print("%s is not getting out of the penalty box" % self.players[self.current_player])
            self.is_getting_out_of_penalty_box = False

    def _ask_question(self):
        self._ask_question_for_category("Science", self.science_questions)
        self._ask_question_for_category("Pop", self.pop_questions)
        self._ask_question_for_category("Sports", self.sports_questions)
        self._ask_question_for_category("Rock", self.rock_questions)

    def _ask_question_for_category(self, label, list):
        if self._current_category == label:
            if len(list) > 0:
                print(list.pop(0))
            else:
                self.populate_list(label, list)
                print(list.pop(0))

    def populate_list(self, label, list):
        for i in range(self.number_of_questions_in_category):
            list.append("%s Question %s" % (label, i))

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                      ' now has ' + \
                      str(self.purses[self.current_player]) + \
                      ' Gold Coins.')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            print("Answer was correct!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                  ' now has ' + \
                  str(self.purses[self.current_player]) + \
                  ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    # Player needs 6 coins to win
    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


from random import randrange


def play(number_of_questions):
    not_a_winner = False
    game = Game(number_of_questions)
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')
    while True:
        game.roll(randrange(1, 7))

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break


if __name__ == '__main__':
    play(5)
