import string
import re
import os
from pathlib import Path

# import configs
TRUE_CASER_COUNT_FILE = os.environ['TRUE_CASER_COUNT_FILE']
TRAINING_PATH = os.environ['TRAINING_PATH']
PREPROCESS_REMOVE_PUNCTUATION = os.environ['PREPROCESS_REMOVE_PUNCTUATION']
PREPROCESS_REMOVE_NUMBERS = os.environ['PREPROCESS_REMOVE_NUMBERS']

root_path = Path(__file__).parent.parent
true_caser_path = str(root_path.parent) + TRAINING_PATH + TRUE_CASER_COUNT_FILE


def preprocess(line):
    line = _remove_start_end_whitespaces(line)
    if PREPROCESS_REMOVE_PUNCTUATION:
        line = _remove_punctuation(line)
    if PREPROCESS_REMOVE_NUMBERS:
        line = _remove_numbers(line)
    return line


# remove symbols like  [!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~]
def _remove_punctuation(line):
    return line.translate(str.maketrans('', '', string.punctuation))


def _remove_numbers(line):
    #   return re.sub(r'\d +', '', line)
    return re.sub('[0-9]+', '', line)


def _remove_start_end_whitespaces(line):
    """
    Removes whitespace, if it is at the beginning or end of the line
    :param line:
    :return:
    """
    return line.strip()
