import string
import re
from pathlib import Path
from generation.true_caser import TrueCaser
from config import TRUE_CASER_ACTIVE, TRUE_CASER_COUNT_FILE, DEFAULT_TRAINING_PATH

root_path = Path(__file__).parent.parent
true_caser_path = str(root_path.parent) + DEFAULT_TRAINING_PATH + TRUE_CASER_COUNT_FILE


class LinePreprocessor():

    def __init__(self):
        if TRUE_CASER_ACTIVE:
            self.true_caser = TrueCaser()
            self.true_caser.import_counter(true_caser_path)
            self.true_caser.close_training()

    def preprocess(self, line):
        #TODO keep in or out?
        # line = self._remove_numbers(line)
        # line = self._remove_punctuation(line)
        line = self._remove_start_end_whitespaces(line)

        if TRUE_CASER_ACTIVE:
            tokenized = ''
            for token in line.split():
                tokenized += self.true_caser.true_case(token) + ' '
            tokenized = tokenized[:-1]
            return tokenized
        return line

    def preprocess_lines(self, lines):
        lines = list(map(self._remove_numbers, lines))
        lines = list(map(self._remove_punctuation, lines))
        lines = list(map(self._remove_start_end_whitespaces, lines))
        lines = true_case_lines(lines)
        return lines

    # remove symbols like  [!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~]
    def _remove_punctuation(self, line):
        return line.translate(str.maketrans('', '', string.punctuation))

    def _remove_numbers(self, line):
        #   return re.sub(r'\d +', '', line)
        return re.sub('[0-9]+', '', line)

    def _remove_start_end_whitespaces(self, line):
        """
        Removes whitespace, if it is at the beginning or end of the line
        :param line:
        :return:
        """
        return line.strip()
