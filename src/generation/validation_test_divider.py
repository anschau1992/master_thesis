import logging
import types
from random import randint


class ValidationTestDivider:

    def __init__(self, validation_ratio, test_ratio):
        if not (0.00 <= validation_ratio <= 1.00) or not (0.00 <= test_ratio <= 1.00):
            raise Exception('Ratios can not be smaller than 0.00 and bigger than 1.00')
        if (validation_ratio + test_ratio) > 1.00:
            raise Exception('The sum of the ratios is higher than 1.00, which is illegal.')

        self.validation_ratio = int(validation_ratio * 100)  # easier to count with whole numbers
        self.test_ratio = int(test_ratio * 100)  # easier to count with whole numbers
        self.total_count = 0
        self.train_count = 0
        self.val_count = 0
        self.test_count = 0

    def divide_data(self, sources_en: list, sources_de: list, targets_de: list, base_de: list):
        if len(sources_en) != len(sources_de) or len(sources_en) != len(targets_de) or len(sources_en) != len(base_de):
            raise Exception('Length of the data-sets provided is not equal')

        validation_data_set = types.SimpleNamespace()
        validation_data_set.sources_en = []
        validation_data_set.sources_de = []
        validation_data_set.targets_de = []
        validation_data_set.base_de = []

        test_data_set = types.SimpleNamespace()
        test_data_set.sources_en = []
        test_data_set.sources_de = []
        test_data_set.targets_de = []
        test_data_set.base_de = []

        training_data_set = types.SimpleNamespace()
        training_data_set.sources_en = []
        training_data_set.sources_de = []
        training_data_set.targets_de = []
        training_data_set.base_de = []

        for i in range(len(sources_en)):
            if 0 <= (self.total_count % 100) < self.validation_ratio:
                # put into validation set
                validation_data_set.sources_en.append(sources_en[i])
                validation_data_set.sources_de.append(sources_de[i])
                validation_data_set.targets_de.append(targets_de[i])
                validation_data_set.base_de.append(base_de[i])
                self.val_count += 1

            elif self.validation_ratio <= (self.total_count % 100) <= (self.validation_ratio + self.test_ratio):
                # put into test set
                test_data_set.sources_en.append(sources_en[i])
                test_data_set.sources_de.append(sources_de[i])
                test_data_set.targets_de.append(targets_de[i])
                test_data_set.base_de.append(base_de[i])
                self.test_count += 1
            else:
                # put into training set
                training_data_set.sources_en.append(sources_en[i])
                training_data_set.sources_de.append(sources_de[i])
                training_data_set.targets_de.append(targets_de[i])
                training_data_set.base_de.append(base_de[i])
                self.train_count += 1

            self.total_count += 1

        return training_data_set, validation_data_set, test_data_set

    def get_total_count(self):
        return self.total_count

    def get_train_count(self):
        return self.train_count

    def get_val_count(self):
        return self.val_count

    def get_test_count(self):
        return self.test_count

    def get_validation_ratio(self):
        return self.validation_ratio

    def get_test_ratio(self):
        return self.test_ratio
