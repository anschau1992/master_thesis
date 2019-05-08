import unittest
from generation.true_caser import build_model, truecase


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
        model = build_model(input_list)
        result = truecase("Never APPeared", model)
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
        model = build_model(input_list)
        result = truecase("capitalize", model)
        self.assertEqual("Capitalize", result)