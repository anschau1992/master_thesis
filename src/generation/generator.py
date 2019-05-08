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