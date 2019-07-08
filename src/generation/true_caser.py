"""
 Simple True-caser & Top-Most validator

    For simplicity reasons it only compares the count of
    lowercase against capitalized version of a token.
    This method assumes that all punctuations are removed beforehand.

    Also used as an Top-Most validator, as it holds the counts for all the tokens.
    Can evaluate the

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
        :raises Exception if training has not finished yet
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

    def is_true_case_most_common(self, token, n):
        """
        Is the true-case form of the given token
        one of the n-th common token in the model
        :param token:
        :param n:
        :raises Exception if training has not finished yet.
        :return:
        """
        if not self.has_training_finished:
            raise Exception('Training of the true-caser has not finished yet.'
                            ' Close it by calling "close_training"-function.')
        most_common = self.true_case_counter.most_common(n)
        true_case = self.true_case(token)
        token_count = self.true_case_counter[true_case]
        return most_common.__contains__((true_case, token_count))
