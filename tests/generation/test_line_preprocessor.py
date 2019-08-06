import unittest
from src.generation.line_preprocessor import _remove_punctuation, _remove_numbers, _remove_start_end_whitespaces


class TestLinePreprocessor(unittest.TestCase):

    def test_remove_punctuation(self):
        """
        Test if the punctuations are removed
        :return: line without punctuation
        """
        input_str = "This &is [an] example? {of} string. with.? punctuation!!!!"
        preprocessed_string = _remove_punctuation(input_str)
        self.assertEqual(preprocessed_string, 'This is an example of string with punctuation')

    def test_remove_numbers(self):
        """
        Test if the numbers of a string are removed
        :return: line without numbers
        """
        input_str = "Box A contains 3red and 54white balls, while Box B contains 4 red and 2 blue balls."
        preprocessed_string = _remove_numbers(input_str)
        self.assertEqual('Box A contains red and white balls, while Box B contains  red and  blue balls.',
                         preprocessed_string,)

    def test_remove_start_end_whitespaces(self):
        input_str = " \t a string example\t "
        preprocessed_string = _remove_start_end_whitespaces(input_str)
        self.assertEqual('a string example', preprocessed_string)
