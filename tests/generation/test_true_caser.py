import unittest
from generation.true_caser import TrueCaser


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
        the method "true-case" returns the lowered form of the word.
        :return: lowered form of word "test"
        """
        true_caser = TrueCaser()
        true_caser.train('Test')
        true_caser.train('test')
        true_caser.train('test')
        true_caser.train('Test')

        true_caser.close_training()
        self.assertEqual('test', true_caser.true_case('Test'))

    def test_no_training_true_case(self):
        """
        Is the model never trained with any form of a token,
        it returns the lower form of the token.
        :return: lowered form of word "test"
        """
        true_caser = TrueCaser()
        true_caser.close_training()
        self.assertEqual('test', true_caser.true_case('Test'))
