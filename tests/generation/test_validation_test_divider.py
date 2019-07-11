import unittest
from src.generation.validation_test_divider import ValidationTestDivider

# example data used in multiple tests
test_source_en = [
    'Record file and application usage',
    'Record file and application usage',
    'Record file and application usage',
    'Record file and application usage',
    'Record file and application usage',
    'Record file and application usage',
    'Record file and application usage',
]
test_source_de = [
    'der\n',
    'Nutzung\n',
    'von\n',
    'Datei\n',
    'und\n',
    'Anwendung\n',
    'aufzeichnen\n'
]
test_targets_de = [
    'Die\n',
    'Nutzung\n',
    'von\n',
    'Dateien\n',
    'und\n',
    'Anwendungen\n',
    'aufzeichnen\n'
]

test_base_de = [
    'Die Nutzung von Dateien und Anwendungen aufzeichnen',
    'Die Nutzung von Dateien und Anwendungen aufzeichnen',
    'Die Nutzung von Dateien und Anwendungen aufzeichnen',
    'Die Nutzung von Dateien und Anwendungen aufzeichnen',
    'Die Nutzung von Dateien und Anwendungen aufzeichnen',
    'Die Nutzung von Dateien und Anwendungen aufzeichnen',
    'Die Nutzung von Dateien und Anwendungen aufzeichnen',
]

test_wrong_length = [
    'only',
    'length',
    'of',
    'four'
]


class TestSplitValidationTestData(unittest.TestCase):

    def test_too_high_validation_ratio(self):
        """
        Validation ratio, provided as param,
        must be between 0.00 and 1.00.
        Higher ratio throws an error.
        :return:
        """
        self.assertRaises(Exception, ValidationTestDivider, 1.20, 0.30)

    def test_too_high_testing_ratio(self):
        """
        Testing ratio, provided as param,
        must be between 0.00 and 1.00.
        Higher ratio throws an error.
        :return:
        """
        self.assertRaises(Exception, ValidationTestDivider, 0.30, 1.20)

    def test_too_low_validation_ratio(self):
        """
        Validation ratio, provided as param,
        must be between 0.00 and 1.00.
        Lower ratio throws an error.
        :return:
        """
        self.assertRaises(Exception, ValidationTestDivider, -0.10, 0.20)

    def test_too_low_testing_ratio(self):
        """
        Testing ratio, provided as param,
        must be between 0.00 and 1.00.
        Lower ratio throws an error.
        :return:
        """
        self.assertRaises(Exception, ValidationTestDivider, 0.20, -0.10)

    def test_too_high_sum_ratio(self):
        """
        The sum of the two ratios cannot be higher than 1.00.
        Throws exception if so
        :return:
        """
        self.assertRaises(Exception, ValidationTestDivider, 0.50, 0.60)

    def test_proper_ratio_initialization(self):
        """
        Proper ratios initialises the divider with line-count 0.
        :return:
        """
        valtest_divider = ValidationTestDivider(0.50, 0.40)

        self.assertEqual(valtest_divider.get_data_count(), 0)
        self.assertEqual(valtest_divider.get_validation_ratio(), 50)
        self.assertEqual(valtest_divider.get_test_ratio(), 40)

    # DIVIDE METHOD

    def test_non_equal_params_length_01(self):
        """
        All the parameters must be a list with the same length.
        Throws exception if first has other length.
        :return:
        """
        valtest_divider = ValidationTestDivider(0.50, 0.40)
        self.assertRaises(Exception,
                          valtest_divider.divide_data, test_wrong_length,
                          test_source_de, test_targets_de, test_base_de
                          )

    def test_non_equal_params_length_02(self):
        """
        All the parameters must be a list with the same length.
        Throws exception if second has other length.
        :return:
        """
        valtest_divider = ValidationTestDivider(0.50, 0.40)
        self.assertRaises(Exception,
                          valtest_divider.divide_data, test_source_en,
                          test_wrong_length, test_targets_de, test_base_de
                          )

    def test_non_equal_params_length_03(self):
        """
        All the parameters must be a list with the same length.
        Throws exception if third has other length.
        :return:
        """
        valtest_divider = ValidationTestDivider(0.50, 0.40)

        self.assertRaises(Exception,
                          valtest_divider.divide_data, test_source_en,
                          test_source_de, test_wrong_length, test_base_de
                          )

    def test_non_equal_params_length_04(self):
        """
        All the parameters must be a list with the same length.
        Throws exception if fourth has other length.
        :return:
        """
        valtest_divider = ValidationTestDivider(0.50, 0.40)

        self.assertRaises(Exception,
                          valtest_divider.divide_data, test_source_en,
                          test_source_de, test_targets_de, test_wrong_length
                          )

    def test_proper_divide(self):
        """
        Division according to ratio is done properly
        :return:
        """
        valtest_divider = ValidationTestDivider(0.02, 0.02)
        training_data_set, validation_data_set, test_data_set =\
            valtest_divider.divide_data(
                test_source_en, test_source_de, test_targets_de, test_base_de
            )
        self.assertEqual(len(validation_data_set.sources_de), 2)
        self.assertEqual(len(test_data_set.sources_de), 2)
        self.assertEqual(len(training_data_set.sources_de), 3)

    def test_proper_divide_multiple(self):
        """
        Division according to ratio is done properly also over multiple function calls.
        Depending on the "data_count" of the class, the class divides accordingly.

        Put in 105 lines by a ratio of 0.30/0.40/0.30:
        -> 35/40/30 lines for val/test/train
        :return:
        """
        valtest_divider = ValidationTestDivider(0.30, 0.40)

        training_sources_de = []
        validation_sources_de = []
        test_sources_de = []

        for i in range(0, 15):
            new_train, new_val, new_test =\
                valtest_divider.divide_data(
                    test_source_en, test_source_de, test_targets_de, test_base_de
                )
            training_sources_de = training_sources_de + new_train.sources_de
            validation_sources_de = validation_sources_de + new_val.sources_de
            test_sources_de = test_sources_de + new_test.sources_de

        self.assertEqual(30, len(training_sources_de))
        self.assertEqual(35, len(validation_sources_de))
        self.assertEqual(40, len(test_sources_de))

    def test_zero_ratio_leaves_empty(self):
        """
        Provide a ratio of 0.00 as parameter leaves does not do any division at all.
        :return:
        """
        valtest_divider = ValidationTestDivider(0.00, 0.00)

        training_sources_de = []
        validation_sources_de = []
        test_sources_de = []

        for i in range(0, 15):
            new_train, new_val, new_test = \
                valtest_divider.divide_data(
                    test_source_en, test_source_de, test_targets_de, test_base_de
                )
            training_sources_de = training_sources_de + new_train.sources_de
            validation_sources_de = validation_sources_de + new_val.sources_de
            test_sources_de = test_sources_de + new_test.sources_de

        self.assertEqual(105, len(training_sources_de))
        self.assertEqual(0, len(validation_sources_de))
        self.assertEqual(0, len(test_sources_de))

