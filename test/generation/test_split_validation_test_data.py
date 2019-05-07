import unittest
from src.generation.generator import split_validation_and_test_data

# example data used in multiple tests
basic_source_en = [
    'Change your own user data',
    'Change your own user data',
    'Change your own user data'
]
basic_source_de = [
    'sich',
    'eigen',
    'Benutzerdaten',
]
basic_targets_de = [
    'Ihrer',
    'eigenen',
    'Benutzerdaten',
]


class TestSplitValidationTestData(unittest.TestCase):

    def test_correct_returning_attributes(self):
        """
        The three returning object all contains three lists named:
        - sources_en
        - sources_de
        - targets_de
        :return: this three objects
        """
        training_data, validation_data, test_data = \
            split_validation_and_test_data(basic_source_en, basic_source_en, basic_targets_de, 0.1, 0.2)

        # training data
        self.assertTrue(hasattr(training_data, 'sources_en'))
        self.assertTrue(hasattr(training_data, 'sources_de'))
        self.assertTrue(hasattr(training_data, 'targets_de'))

        # validation data
        self.assertTrue(hasattr(validation_data, 'sources_en'))
        self.assertTrue(hasattr(validation_data, 'sources_de'))
        self.assertTrue(hasattr(validation_data, 'targets_de'))

        # test data
        self.assertTrue(hasattr(test_data, 'sources_en'))
        self.assertTrue(hasattr(test_data, 'sources_de'))
        self.assertTrue(hasattr(test_data, 'targets_de'))

    def test_no_ratios_provided(self):
        """
        Parameter 4 and 5 need to be ratios between 0.00 and 1.00
        :return: exception as no ratios provided
        """
        self.assertRaises(Exception, split_validation_and_test_data,
                          basic_source_en, basic_source_de, basic_targets_de)

    def test_too_high_ratio_one_provided(self):
        """
        Parameter 4 and 5 need to be ratios between 0.00 and 1.00.
        Higher ratios raises Exception.
        :return: exception
        """
        self.assertRaises(Exception, split_validation_and_test_data,
                          basic_source_en, basic_source_de, basic_targets_de, 0.1, 1.5)

    def test_incorrect_ratio_two_provided(self):
        """
        Parameter 4 and 5 need to be ratios between 0.00 and 1.00.
        Higher ratios raises Exception.
        :return: exception
        """
        self.assertRaises(Exception, split_validation_and_test_data,
                          basic_source_en, basic_source_de, basic_targets_de, 1.5, 0.1)

    def test_too_low_ratio_one_provided(self):
        """
        Parameter 4 and 5 need to be ratios between 0.00 and 1.00.
        Lower ratios raises Exception.
        :return: exception
        """
        self.assertRaises(Exception, split_validation_and_test_data,
                          basic_source_en, basic_source_de, basic_targets_de, -0.1, 0.2)

    def test_too_low_ratio_two_provided(self):
        """
        Parameter 4 and 5 need to be ratios between 0.00 and 1.00.
        Lower ratios raises Exception.
        :return: exception
        """
        self.assertRaises(Exception, split_validation_and_test_data,
                          basic_source_en, basic_source_de, basic_targets_de, 0.2, -0.1)

    def test_ratio_sum_higher_than_one(self):
        """
        Parameter 4 and 5 need to be ratios between 0.00 and 1.00.
        Is the sum of the two higher than 1 it is illogical.
        :return: exception as sum is higher than 1
        """
        self.assertRaises(Exception, split_validation_and_test_data,
                          basic_source_en, basic_source_de, basic_targets_de, 0.6, 0.5)

    def test_empty_paramters(self):
        """
        Empty parameter entries should return empty lists back
        :return: three objects including three empty lists
        """
        training_data, validation_data, test_data = split_validation_and_test_data([], [], [], 0.1, 0.2)

        # training data
        self.assertEqual(len(training_data.sources_en), 0)
        self.assertEqual(len(training_data.sources_de), 0)
        self.assertEqual(len(training_data.targets_de), 0)

        # validation data
        self.assertEqual(len(validation_data.targets_de), 0)
        self.assertEqual(len(validation_data.targets_de), 0)
        self.assertEqual(len(validation_data.targets_de), 0)

        # test data
        self.assertEqual(len(test_data.targets_de), 0)
        self.assertEqual(len(test_data.targets_de), 0)
        self.assertEqual(len(test_data.targets_de), 0)

    def test_not_same_length_01(self):
        """
        Not the same length of the three lists raises an exception.
        :return: Exception, as param 1 has four entries.
        """
        source_en = [
            'Change your own user data',
            'Change your own user data',
            'Change your own user data',
            'Change your own user data',
        ]
        source_de = [
            'sich',
            'eigen',
            'Benutzerdaten',
        ]
        targets_de = [
            'Ihrer',
            'eigenen',
            'Benutzerdaten',
        ]

        self.assertRaises(Exception, split_validation_and_test_data,
                          source_en, source_de, targets_de, 0.1, 0.1)

    def test_not_same_length_02(self):
        """
        Not the same length of the three lists raises an exception.
        :return: Exception, as param 2 has four entries.
        """
        source_en = [
            'Change your own user data',
            'Change your own user data',
            'Change your own user data',
        ]
        source_de = [
            'sich',
            'eigen',
            'Benutzerdaten',
            'Ändern',
        ]
        targets_de = [
            'Ihrer',
            'eigenen',
            'Benutzerdaten',
        ]

        self.assertRaises(Exception, split_validation_and_test_data,
                          source_en, source_de, targets_de, 0.1, 0.1)

    def test_not_same_length_03(self):
        """
        Not the same length of the three lists raises an exception.
        :return: Exception, as param 3 has four entries.
        """
        source_en = [
            'Change your own user data',
            'Change your own user data',
            'Change your own user data',
        ]
        source_de = [
            'sich',
            'eigen',
            'Benutzerdaten',
        ]
        targets_de = [
            'Ihrer',
            'eigenen',
            'Benutzerdaten',
            'Ändern',
        ]

        self.assertRaises(Exception, split_validation_and_test_data,
                          source_en, source_de, targets_de, 0.1, 0.1)

    def test_correct_splitting(self):
        """
        Given the ratios the function split the data set correctly
        :return: training-length: 7, validation: 1, testing: 2
        """
        source_en = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        source_de = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        targets_de = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        training_data, validation_data, test_data = \
            split_validation_and_test_data(source_en, source_de, targets_de, 0.1, 0.2)

        # training
        self.assertEqual(len(training_data.sources_en), 7)
        self.assertEqual(len(training_data.sources_de), 7)
        self.assertEqual(len(training_data.targets_de), 7)

        # validation
        self.assertEqual(len(validation_data.targets_de), 1)
        self.assertEqual(len(validation_data.targets_de), 1)
        self.assertEqual(len(validation_data.targets_de), 1)

        # test
        self.assertEqual(len(test_data.targets_de), 2)
        self.assertEqual(len(test_data.targets_de), 2)
        self.assertEqual(len(test_data.targets_de), 2)

    def test_splitting_removes_sources_en_data(self):
        """
        When a String is taken from training into e.g. validation or test set,
        it is not in training set anymore
        Only done on sources_en
        :return:
        """
        source_en = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        source_de = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        targets_de = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        training_data, validation_data, test_data = \
            split_validation_and_test_data(source_en, source_de, targets_de, 0.3, 0.3)

        for entry in validation_data.sources_en:
            if entry in training_data.sources_en:
                self.fail("Entry %d was found in the Validation set and Training set" % entry)

        for entry in test_data.sources_en:
            if entry in training_data.sources_en:
                self.fail("Entry %d was found in the Test set and Training set" % entry)

    def test_splitting_removes_sources_de_data(self):
        """
        When a String is taken from training into e.g. validation or test set,
        it is not in training set anymore
        Only done on sources_de
        :return:
        """
        source_en = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        source_de = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        targets_de = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        training_data, validation_data, test_data = \
            split_validation_and_test_data(source_en, source_de, targets_de, 0.3, 0.3)

        for entry in validation_data.sources_de:
            if entry in training_data.sources_de:
                self.fail("Entry %d was found in the Validation set and Training set" % entry)

        for entry in test_data.sources_en:
            if entry in training_data.sources_de:
                self.fail("Entry %d was found in the Test set and Training set" % entry)

    def test_splitting_removes_targets_de_data(self):
        """
        When a String is taken from training into e.g. validation or test set,
        it is not in training set anymore
        Only done on sources_en
        :return:
        """
        source_en = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        source_de = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        targets_de = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        training_data, validation_data, test_data = \
            split_validation_and_test_data(source_en, source_de, targets_de, 0.3, 0.3)

        for entry in validation_data.targets_de:
            if entry in training_data.targets_de:
                self.fail("Entry %d was found in the Validation set and Training set" % entry)

        for entry in test_data.targets_de:
            if entry in training_data.targets_de:
                self.fail("Entry %d was found in the Test set and Training set" % entry)
