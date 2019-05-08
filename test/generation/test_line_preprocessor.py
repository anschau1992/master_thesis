import unittest
from generation.line_preprocessor import _remove_punctuation


class TestLinePreprocessor(unittest.TestCase):

    def test_remove_punctuation(self):
        """
        Test if the punctuations are removed
        :return: line without punctuation
        """
        input_str = "This &is [an] example? {of} string. with.? punctuation!!!!"
        preprocessed_string = _remove_punctuation(input_str)
        self.assertEqual(preprocessed_string, 'This is an example of string with punctuation')
