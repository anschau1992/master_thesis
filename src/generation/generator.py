import sys
import logging
import spacy
import types
from random import randint
from spacy.tokenizer import Tokenizer

module = sys.modules['__main__'].__file__
log = logging.getLogger(module)
nlp = spacy.load("de")
tokenizer = Tokenizer(nlp.vocab)


def generate_train_data(lines_en, lines_de):
    """
    Generates the training data in lists.
    Entries with the same position are considered a tuple
    :param lines_en:
    :param lines_de:
    :return: three lists - source english, source german, target german
    """
    logging.info('Generator: Start generating training data')

    if len(lines_en) != len(lines_de):
        raise Exception('Length of the list parameters are not equal')

    sources_en = []
    sources_de = []
    targets_de = []

    for i in range(0, len(lines_en)):
        line_en = lines_en[i]
        line_de = lines_de[i]

        tokens = nlp(line_de)
        for token in tokens:
            line_en = __assure_line_break(line_en)
            sources_en.append(line_en)

            lemma = __assure_line_break(token.lemma_)
            sources_de.append(lemma)

            token_string = __assure_line_break(str(token))
            targets_de.append(token_string)

    logging.debug("Finish generate training data. Number of entries: %s " % len(lines_de))
    return sources_en, sources_de, targets_de


def __assure_line_break(line):
    if not '\n' in line:
        return line + '\n'
    return line


def split_validation_and_test_data(sources_en: object, sources_de: object, targets_de: object, validation_ratio: object, test_ratio: object) -> object:
    logging.info('Generator: Splitting data into training/test/validation sets')

    if not (0.00 <= validation_ratio <= 1.00) or not (0.00 <= test_ratio <= 1.00):
        raise Exception('Ratios can not be smaller than 0.00 and bigger than 1.00')

    if (validation_ratio + test_ratio) > 1.00:
        raise Exception('The sum of the ratios is higher than 1.00, which is illegal.')

    if len(sources_en) != len(sources_de) or len(sources_en) != len(targets_de):
        raise Exception('Length of the data-sets provided is not equal')

    set_length = len(sources_de)
    validation_set_number = int(set_length * validation_ratio)
    test_set_number = int(set_length * test_ratio)

    validation_data_set = types.SimpleNamespace()
    validation_data_set.sources_en = []
    validation_data_set.sources_de = []
    validation_data_set.targets_de = []

    for i in range(0, validation_set_number):
        random_position = randint(0, len(sources_en)-1)
        validation_data_set.sources_en.append(sources_en.pop(random_position))
        validation_data_set.sources_de.append(sources_de.pop(random_position))
        validation_data_set.targets_de.append(targets_de.pop(random_position))

    test_data_set = types.SimpleNamespace()
    test_data_set.sources_en = []
    test_data_set.sources_de = []
    test_data_set.targets_de = []

    for i in range(0, test_set_number):
        random_position = randint(0, len(sources_en)-1)
        test_data_set.sources_en.append(sources_en.pop(random_position))
        test_data_set.sources_de.append(sources_de.pop(random_position))
        test_data_set.targets_de.append(targets_de.pop(random_position))

    training_data_set = types.SimpleNamespace()
    training_data_set.sources_en = sources_en
    training_data_set.sources_de = sources_de
    training_data_set.targets_de = targets_de

    return training_data_set, validation_data_set, test_data_set