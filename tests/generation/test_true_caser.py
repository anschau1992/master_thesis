import unittest
from generation.true_caser import _build_model, _true_case, true_case_lines


class TestTrueCaser(unittest.TestCase):

    def test_no_corpus_appearance(self):
        """
        If a token has not appeared in the corpus. The true-case should return it as lowercase
        :return: lowercase word
        """
        input_list = [
            "Hello world",
            "Simple test",
            "for the true caser"
        ]
        model = _build_model(input_list)
        result = _true_case("Never APPeared", model)
        self.assertEqual("never appeared", result)

    def test_correct_capitalization(self):
        """
        If a token was more times capitalised in the model,
         the it should get capitalized by the true-caser
        :return:
        """
        input_list = [
            "Capitalize this",
            "capitalize",
            "Second time Capitalize"
        ]
        model = _build_model(input_list)
        result = _true_case("capitalize", model)
        self.assertEqual("Capitalize", result)

    def test_true_case_lines(self):
        """
        Test if the true-caser return the expected lines, given the input
        :return:
        """
        input_list = [
            "lower Up",
            "Up up",
            "Lower lower lower"
        ]
        result = true_case_lines(input_list)
        self.assertEqual([
            "lower Up",
            "Up Up",
            "lower lower lower"
        ], result)