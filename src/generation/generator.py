import sys
import logging
import spacy
from pathlib import Path
from generation.true_caser import TrueCaser
from spacy.tokenizer import Tokenizer
from config import PREPROCESS_TRUE_CASER, DEFAULT_TRAINING_PATH, TRUE_CASER_COUNT_FILE
from generation.line_preprocessor import preprocess

root_path = Path(__file__).parent.parent
true_caser_path = str(root_path.parent) + DEFAULT_TRAINING_PATH + TRUE_CASER_COUNT_FILE

module = sys.modules['__main__'].__file__
log = logging.getLogger(module)
nlp = spacy.load("de")
tokenizer = Tokenizer(nlp.vocab)

# import True_caser learnings
if PREPROCESS_TRUE_CASER:
    true_caser = TrueCaser()
    true_caser.import_counter(true_caser_path)
    true_caser.close_training()


def generate_train_data(line_en, line_de):
    if type(line_en) is not str or type(line_de) is not str:
        raise Exception('Provided parameters are not of type string')

    line_en = preprocess(line_en)
    line_de = preprocess(line_de)

    sources_en = []
    sources_de = []
    targets_de = []
    base_de = []

    tokens = nlp(line_de, disable=['parser', 'tagger', 'ner'])
    for token in tokens:
        # skip too short tokens like e.g. 'it'
        if len(token) >= 2:

            line_en = __assure_line_break(line_en)
            sources_en.append(line_en)

            lemma = __assure_line_break(token.lemma_)
            sources_de.append(lemma)

            if PREPROCESS_TRUE_CASER:
                token = true_caser.true_case(token)

            token_string = __assure_line_break(str(token))
            targets_de.append(token_string)

            base_de.append(__assure_line_break(line_de))
    return sources_en, sources_de, targets_de, base_de


def __assure_line_break(line):
    if not '\n' in line:
        return line + '\n'
    return line
