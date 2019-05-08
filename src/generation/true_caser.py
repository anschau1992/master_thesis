"""
 Simple True-caser

 For simplicity reasons it only compares the count of
  lowercase against capitalized version of a token.

"""
import logging
from collections import Counter


def build_model(lines):
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


def truecase(line, model):
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