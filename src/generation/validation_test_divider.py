import logging
import types
from random import randint


class ValidationTestDivider():

    def __init(self, validation_ratio, test_ratio):
        if not (0.00 <= validation_ratio <= 1.00) or not (0.00 <= test_ratio <= 1.00):
            raise Exception('Ratios can not be smaller than 0.00 and bigger than 1.00')
        if (validation_ratio + test_ratio) > 1.00:
            raise Exception('The sum of the ratios is higher than 1.00, which is illegal.')

        self.validation_ratio = validation_ratio * 100  # easier to count with whole numbers
        self.test_ratio = test_ratio * 100  # easier to count with whole numbers
        self.data_count = 0

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
        training_data_set.sources_en = sources_en
        training_data_set.sources_de = sources_de
        training_data_set.targets_de = targets_de
        training_data_set.base_de = base_de

        for i in range(len(sources_en)):
            if 0 < (self.data_count % 100) <= self.validation_ratio:
                # put into validation set
                validation_data_set.sources_en.append(sources_en[i])
                validation_data_set.sources_de.append(sources_de[i])
                validation_data_set.targets_de.append(targets_de[i])
                validation_data_set.base_de.append(base_de.pop[i])

            elif self.validation_ratio < (self.data_count % 100) <= self.test_ratio:
                # put into test set
                test_data_set.sources_en.append(sources_en[i])
                test_data_set.sources_de.append(sources_de[i])
                test_data_set.targets_de.append(targets_de[i])
                test_data_set.base_de.append(base_de[i])
            else:
                # put into training set
                training_data_set.sources_en.append(sources_en[i])
                training_data_set.sources_de.append(sources_en[i])
                training_data_set.targets_de.append(sources_en[i])
                training_data_set.base_de.append(sources_en[i])

            self.data_count += 1

        return training_data_set, validation_data_set, test_data_set

    def get_data_count(self):
        return self.data_count

    def divide_data_by_lines(self, sources_en: object, sources_de: object, targets_de: object, base_de: object,
                             validation_ratio: object,
                             test_ratio: object) -> object:
        logging.info('Generator: Splitting data into training/test/validation sets')

        if not (0.00 <= validation_ratio <= 1.00) or not (0.00 <= test_ratio <= 1.00):
            raise Exception('Ratios can not be smaller than 0.00 and bigger than 1.00')

        if (validation_ratio + test_ratio) > 1.00:
            raise Exception('The sum of the ratios is higher than 1.00, which is illegal.')

        if len(sources_en) != len(sources_de) or len(sources_en) != len(targets_de) or len(sources_en) != len(base_de):
            raise Exception('Length of the data-sets provided is not equal')

        set_length = len(sources_de)
        validation_set_number = int(set_length * validation_ratio)
        test_set_number = int(set_length * test_ratio)

        validation_data_set = types.SimpleNamespace()
        validation_data_set.sources_en = []
        validation_data_set.sources_de = []
        validation_data_set.targets_de = []
        validation_data_set.base_de = []

        for i in range(0, validation_set_number):
            random_position = randint(0, len(sources_en) - 1)
            validation_data_set.sources_en.append(sources_en.pop(random_position))
            validation_data_set.sources_de.append(sources_de.pop(random_position))
            validation_data_set.targets_de.append(targets_de.pop(random_position))
            validation_data_set.base_de.append(base_de.pop(random_position))

        test_data_set = types.SimpleNamespace()
        test_data_set.sources_en = []
        test_data_set.sources_de = []
        test_data_set.targets_de = []
        test_data_set.base_de = []

        for i in range(0, test_set_number):
            random_position = randint(0, len(sources_en) - 1)
            test_data_set.sources_en.append(sources_en.pop(random_position))
            test_data_set.sources_de.append(sources_de.pop(random_position))
            test_data_set.targets_de.append(targets_de.pop(random_position))
            test_data_set.base_de.append(base_de.pop(random_position))

        training_data_set = types.SimpleNamespace()
        training_data_set.sources_en = sources_en
        training_data_set.sources_de = sources_de
        training_data_set.targets_de = targets_de
        training_data_set.base_de = base_de

        return training_data_set, validation_data_set, test_data_set
