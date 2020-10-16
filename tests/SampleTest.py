import unittest
from contextlib import redirect_stdout

from io import StringIO
import random

from approvaltests.approvals import verify

from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory


class RegressionTest(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get("DiffMerge")
        # Download DiffMerge at https://sourcegear.com/diffmerge/

    def test_straight_unittest(self):
        self.assertEqual(5, 5)

    def test_with_approvals(self):
        from CodeGoesHere import sample
        verify(sample(), self.reporter)

    def test_trivia_with_approvals(self):
        verify(self.play_trivia(0), self.reporter)

    def test_trivia_with_approvals_2(self):
        verify(self.play_trivia(2, 100), self.reporter)

    def play_trivia(self, seed=0, questions=50):
        from Trivia import play
        string_io = StringIO()

        with redirect_stdout(string_io):
            random.seed(seed)
            play(questions)
        return string_io.getvalue()
