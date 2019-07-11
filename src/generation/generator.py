import sys
import logging
import spacy
from spacy.tokenizer import Tokenizer

from generation.line_preprocessor import LinePreprocessor

module = sys.modules['__main__'].__file__
log = logging.getLogger(module)
nlp = spacy.load("de")
tokenizer = Tokenizer(nlp.vocab)
preprocessor = LinePreprocessor()

def generate_train_data(line_en, line_de):
    if type(line_en) is not str or type(line_de) is not str:
        raise Exception('Provided parameters are not of type string')

    line_en = preprocessor.preprocess(line_en)
    line_de = preprocessor.preprocess(line_de)

    sources_en = []
    sources_de = []
    targets_de = []
    base_de = []

    tokens = nlp(line_de)
    for token in tokens:
        # skip too short tokens
        if len(token) >= 2:
            line_en = __assure_line_break(line_en)
            sources_en.append(line_en)

            lemma = __assure_line_break(token.lemma_)
            sources_de.append(lemma)

            token_string = __assure_line_break(str(token))
            targets_de.append(token_string)

            base_de.append(__assure_line_break(line_de))
    return sources_en, sources_de, targets_de, base_de


def generate_train_data_by_lines(lines_en, lines_de):
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

    lines_en = preprocess_lines(lines_en)
    lines_de = preprocess_lines(lines_de)

    sources_en = []
    sources_de = []
    targets_de = []
    base_de = []

    for i in range(0, len(lines_en)):
        line_en = lines_en[i]
        line_de = lines_de[i]

        tokens = nlp(line_de)
        for token in tokens:
            # skip too short tokens
            if len(token) >= 2:
                line_en = __assure_line_break(line_en)
                sources_en.append(line_en)

                lemma = __assure_line_break(token.lemma_)
                sources_de.append(lemma)

                token_string = __assure_line_break(str(token))
                targets_de.append(token_string)

                base_de.append(__assure_line_break(line_de))

    logging.debug("Finish generate training data. Number of entries: %s " % len(lines_de))
    return sources_en, sources_de, targets_de, base_de


def __assure_line_break(line):
    if not '\n' in line:
        return line + '\n'
    return line
