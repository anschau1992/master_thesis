import string
from generation.true_caser import true_case_lines
import re


def preprocess(line):
    line = _remove_numbers(line)
    line = _remove_punctuation(line)
    return _remove_start_end_whitespaces(line)

    # left out TrueCaser --> TODO truecase counter must be done in prior step


def preprocess_lines(lines):
    lines = list(map(_remove_numbers, lines))
    lines = list(map(_remove_punctuation, lines))
    lines = list(map(_remove_start_end_whitespaces, lines))
    lines = true_case_lines(lines)
    return lines


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
