import string
from generation.true_caser import true_case_lines


def preprocess(lines):
    lines = list(map(_remove_punctuation, lines))
    lines = true_case_lines(lines)
    return lines


# remove symbols like  [!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~]
def _remove_punctuation(line):
    return line.translate(str.maketrans('', '', string.punctuation))
