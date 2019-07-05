"""
 Simple True-caser

 For simplicity reasons it only compares the count of
  lowercase against capitalized version of a token.
  This method assumes that all punctuations are removed beforehand

"""
import logging
from collections import Counter


class TrueCaser():

    def __init__(self):
        self.true_case_counter = Counter()
        self.has_training_finished = False

    def train(self, line):
        """
        Add all the token from the param line into the True-Case-Counter.
        The counter is used to evaluate the true-casing afterwards
        :param line:
        :return:
        """
        if self.has_training_finished:
            raise Exception('The training of the TruceCaser model has already finished before this call.')
        for token in line.split():
            self.true_case_counter[token] += 1

    def close_training(self):
        """
        Close the training, after all tokens have been read in by add_into_model Method.
        Assures that the model will not be changed afterwards.
        The model returns always lower form if the count is even (incl. also 0).
        :return:
        """
        self.has_training_finished = True

    def true_case(self, token):
        """
        Returns the true case of the param token based on the pre-trained model
        :param token:
        :return:
        """
        if not self.has_training_finished:
            raise Exception('Training of the true-caser has not finished yet.'
                            ' Close it by calling "close_training"-function.')
        cap_count = self.true_case_counter[token.capitalize()]
        lower_count = self.true_case_counter[token.lower()]

        if cap_count > lower_count:
            return token.capitalize()
        else:
            return token.lower()


def true_case_lines(lines):
    """
    Takes in multiple lines of text.
    Creates a true-case model with the private function and the provided lines.
    Uses this model to true-case all the lines and return them.
    :return: true cased lines
    """
    model = _build_model(lines)

    true_cased_lines = []
    for line in lines:
        true_cased_lines.append(_true_case(line, model))
    return true_cased_lines


def _build_model(lines):
    """
    Builds a true-caser model, which is trained by the arguments.
    Expects a list of strings as argument. These strings get tokenized for the model
    :param lines:
    :return: the trained counter
    """

    logging.info("True-caser model creation")
    corpus = []
    for line in lines:
        corpus += line.split()

    return Counter(corpus)


def _true_case(line, model):
    """
    Recevies the pre-trained counter and decides based on it if
    each token in the line should be lowercased or capitalized.
    :param line: with text
    :param model: pre-trained counter
    :return: true-cased line
    """
    truecased = []
    for token in line.split():
        cap_count = model[token.capitalize()]
        lower_count = model[token.lower()]

        if cap_count > lower_count:
            truecased.append(token.capitalize())
        else:
            truecased.append(token.lower())
    return " ".join(truecased)
