import unittest
from src.generation.true_caser import TrueCaser


class TestTrueCaser(unittest.TestCase):

    def test_true_case_before_closing(self):
        """
        An instance of the true-caser cannot be used for the process of true-casing, before it is closed and training is done
        :return: Exception if "true_case" is called.
        """
        true_caser = TrueCaser()
        self.assertRaises(Exception, true_caser.true_case, 'test')

    def test_true_case_after_closing(self):
        """
        An instance of the true-caser can true-case after if the model has been closed and training is finished.
        :return: the true-case of 'test'
        """
        true_caser = TrueCaser()
        true_caser.close_training()
        self.assertEqual('test', true_caser.true_case('test'))

    def test_train_after_closing(self):
        """
        An instance of the true-caser cannot train anymore after the model has been closed and the training is finished.
        :return: Exception
        """
        true_caser = TrueCaser()
        true_caser.close_training()
        self.assertRaises(Exception, true_caser.train, 'Test line to train with.')

    def test_capitalize_true_case(self):
        """
        Is the model trained with more capitalized form of a word,
        the method "true-case" returns the capitalized form of the word.
        :return: capitalized form of word "test"
        """
        true_caser = TrueCaser()
        true_caser.train('Test')
        true_caser.train('test')
        true_caser.train('Test')

        true_caser.close_training()
        self.assertEqual('Test', true_caser.true_case('test'))

    def test_even_count_true_case(self):
        """
        Is the model trained with the same amount of capitalized and lowered form of a token
        the method "true-case" returns the original form of the word.
        :return: lowered form of word "test"
        """
        true_caser = TrueCaser()
        true_caser.train('Test')
        true_caser.train('test')
        true_caser.train('test')
        true_caser.train('Test')

        true_caser.close_training()
        self.assertEqual('Test', true_caser.true_case('Test'))
        self.assertEqual('test', true_caser.true_case('test'))

    def test_no_training_true_case(self):
        """
        Is the model never trained with any form of a token,
        it returns the original form of the token.
        :return: original form of word "test"
        """
        true_caser = TrueCaser()
        true_caser.close_training()
        self.assertEqual('test', true_caser.true_case('test'))
        self.assertEqual('TEST', true_caser.true_case('TEST'))

    def test_most_common_before_closing(self):
        """
        The method 'us_true_case_most_common' is not allowed to call before the model is closed.
        :raises Exception when called before Method is called.
        """
        true_caser = TrueCaser()
        self.assertRaises(Exception, true_caser.is_true_case_most_common, 'test', 1)

    def test_not_most_common(self):
        """
        Method returns 'False' when token is not in most-common n-th tokens.
        :return: False
        """
        true_caser = TrueCaser()
        true_caser.train('Test your data')
        true_caser.train('Test test data')
        true_caser.train('Test Test data')
        true_caser.train('Test your data')
        true_caser.close_training()
        self.assertFalse(true_caser.is_true_case_most_common('your', 2))

    def test_most_common(self):
        """
        Method returns 'True' when token is in most-common n-th tokens.
        :return: True
        """
        true_caser = TrueCaser()
        true_caser.train('Test your data')
        true_caser.train('Test test data')
        true_caser.train('Test Test data')
        true_caser.train('Test your data')
        true_caser.close_training()
        self.assertTrue(true_caser.is_true_case_most_common('your', 3))

    def test_export_counter(self):
        """
        Test the correct export of the True-Caser counter into a file.
        :return:
        """

        fp = './test-true-case-export.en'
        true_caser = TrueCaser()
        true_caser.train('Test your data')
        true_caser.train('Test test data')
        true_caser.train('Test Test data')
        true_caser.train('Test your data')
        true_caser.close_training()

        true_caser.export_counter(fp)

        with open(fp, 'r') as f:
            line = f.readline()
            self.assertEqual(line, 'Test;5\n')
            line = f.readline()
            self.assertEqual(line, 'your;2\n')
            line = f.readline()
            self.assertEqual(line, 'data;4\n')

    def test_import_counter(self):
        """
        Test the correct import of the True-Caser counter into a file.
        :return:
        """
        fp = './test-true-case-import.en'
        # write into file
        with open(fp, 'w+') as f:
            f.write('Test;5\n')
            f.write('Data;10\n')
            f.write('import;15\n')

        true_caser = TrueCaser()
        true_caser.import_counter('./test-true-case-import.en')
        true_caser.close_training()
        self.assertTrue(true_caser.is_true_case_most_common('Test', 3))
        self.assertTrue(true_caser.is_true_case_most_common('Data', 3))
        self.assertTrue(true_caser.is_true_case_most_common('import', 3))
        self.assertFalse(true_caser.is_true_case_most_common('Fail', 3))


