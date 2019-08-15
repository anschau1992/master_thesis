import sys
import logging
import argparse
import os.path
from pathlib import Path

# read configs

TRAINING_PATH = os.environ["TRAINING_PATH"]
DATA_PATH_DE = os.environ["DATA_PATH_DE"]
DATA_PATH_EN = os.environ["DATA_PATH_EN"]
EVAL_SOURCE_PATH = os.environ["EVAL_SOURCE_PATH"]
EVAL_TARGET_PATH = os.environ["EVAL_TARGET_PATH"]
VALIDATION_FRACTION_PERCENTAGE = os.environ["VALIDATION_FRACTION_PERCENTAGE"]
TEST_FRACTION_PERCENTAGE = os.environ["TEST_FRACTION_PERCENTAGE"]
TEST_TARGET_FILE_DE = os.environ["TEST_TARGET_FILE_DE"]
TEST_OUTPUT_FILE_DE = os.environ["TEST_OUTPUT_FILE_DE"]
SOURCE_DATA_PATH = os.environ["SOURCE_DATA_PATH"]
MOST_COMMON_PATH = os.environ["MOST_COMMON_PATH"]
MOST_COMMON_NUMBER = int(os.environ["MOST_COMMON_NUMBER"])
MOST_COMMON_LIST_DE = os.environ["MOST_COMMON_LIST_DE"]
POS_PATH = os.environ["POS_PATH"]
SCORING_FILE = os.environ["SCORING_FILE"]

root_path = Path().resolve().parent


def parse_command_line_generator(argv):
    """
    Parse command line argument for the data generation.
     See -h option
    :param argv: arguments on the command line must include caller file name.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="increase output verbosity (e.g., -vv is more than -v)")
    parser.add_argument("-ien", "--inputEn",
                        dest="file_en", default=DATA_PATH_EN,
                        help="input file with english sentences",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    parser.add_argument("-ide", "--inputDe",
                        dest="file_de", default=DATA_PATH_DE,
                        help="input file with german sentences",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    parser.add_argument("-o", "--output",
                        dest="output", default=TRAINING_PATH, help="training data folder location",
                        metavar="DIR",
                        type=lambda x: _check_and_create_folder(x))
    parser.add_argument("-pv", "--percentageValidation",
                        dest="perValid", default=VALIDATION_FRACTION_PERCENTAGE, help="validation percentage fraction",
                        type=lambda x: _is_percentage_number(parser, x))
    parser.add_argument("-pt", "--percentageTesting",
                        dest="perTest", default=TEST_FRACTION_PERCENTAGE, help="testing percentage fraction",
                        type=lambda x: _is_percentage_number(parser, x))
    args = parser.parse_args()
    logging.basicConfig(filename='run-me.log', level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')

    logging.debug('Finished parsing command line arguments for the Generator')
    return args


def parse_command_line_evaluator(argv):
    """
    Parse command line argument for the evaluation
    See -h for options
    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="increase output verbosity (e.g., -vv is more than -v)")
    parser.add_argument("-s", "--source",
                        dest="file_source", default=(TRAINING_PATH + TEST_OUTPUT_FILE_DE),
                        help="source file with output of the testing phase",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    parser.add_argument("-t", "--target",
                        dest="file_target", default=(TRAINING_PATH + TEST_TARGET_FILE_DE),
                        help="target file with the gold data the model has to predict",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    parser.add_argument("-o", "--output",
                        dest="output", default=(TRAINING_PATH + SCORING_FILE),
                        help="scoring file location path",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    args = parser.parse_args()
    logging.basicConfig(filename='run-me.log', level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')

    logging.info('Finished parsing command line arguments for the Evaluator')
    return args


def parse_command_line_true_caser(argv):
    """
    Parse command line argument for the true case
    See -h for options
    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="increase output verbosity (e.g., -vv is more than -v)")
    parser.add_argument("-sd", "--source_data",
                        dest="source_data", default=SOURCE_DATA_PATH,
                        help="root folder of the in prior downloaded moses data folder",
                        metavar="FOLDER",
                        type=lambda x: _is_valid_folder(parser, x))
    parser.add_argument("-td", "--training_data",
                        dest="training_data", default=TRAINING_PATH,
                        help="training data folder location",
                        metavar="FOLDER",
                        type=lambda x: _add_root_path(x))
    args = parser.parse_args()
    logging.basicConfig(filename='run-me.log', level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('Finished parsing command line arguments for the True Caser')
    return args


def parse_scoring_no_most_common(argv):
    """
    Parse command line arguments for the scoring evaluation which ignores the most common words
    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="increase output verbosity (e.g., -vv is more than -v)")
    parser.add_argument("-i", "--input",
                        dest="input", default=TRAINING_PATH,
                        help="folder-location for input data, must point to root folder of all test files",
                        metavar="DIR",
                        type=lambda x: _is_valid_folder(parser, x))
    parser.add_argument("-o", "--output",
                        dest="output", default=MOST_COMMON_PATH, help="folder-location for the results",
                        metavar="DIR",
                        type=lambda x: _check_and_create_folder(x))
    parser.add_argument("-mc", "--most-common",
                        dest="most-common", default=MOST_COMMON_NUMBER,
                        help="Ignoring the most common english token."
                             " Number of the most common ignored is defined by the parameter.",
                        type=lambda x: _is_positive_int(parser, x))
    parser.add_argument("-df", "--de-file",
                        dest="de_file", default=MOST_COMMON_LIST_DE,
                        help="file with the most common german words. Descending ordered",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    args = parser.parse_args()
    logging.basicConfig(filename='run-me.log', level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('Finished parsing command line arguments for the Scoring-No-Most-Common')
    return args


def parse_scoring_pos_scoring(argv):
    """
    Parse command line arguments for the scoring evaluation, which considers only some specific POS words e.g. nouns
    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="increase output verbosity (e.g., -vv is more than -v)")
    parser.add_argument("-i", "--input",
                        dest="input", default=TRAINING_PATH,
                        help="folder-location for input data, must point to root folder of all test files",
                        metavar="DIR",
                        type=lambda x: _is_valid_folder(parser, x))
    parser.add_argument("-o", "--output",
                        dest="output", default=POS_PATH, help="folder-location for the results",
                        metavar="DIR",
                        type=lambda x: _check_and_create_folder(x))
    args = parser.parse_args()
    logging.basicConfig(filename='run-me.log', level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('Finished parsing command line arguments for the POS scoring')
    return args


def parse_sampling(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="increase output verbosity (e.g., -vv is more than -v)")
    parser.add_argument("-p", "--path",
                        dest="path", default=TRAINING_PATH,
                        help="folder-location for input data, must point to root folder of all training files",
                        metavar="DIR",
                        type=lambda x: _is_valid_folder(parser, x))
    args = parser.parse_args()
    logging.basicConfig(filename='run-me.log', level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('Finished parsing command line arguments for the oversampler')
    return args

def _check_and_create_folder(path):
    file_path = _add_root_path(path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def _add_root_path(relative_path):
    return str(root_path) + relative_path


def _is_valid_folder(parser, path):
    file_path = _add_root_path(path)
    if not os.path.exists(file_path):
        parser.error("The folder %s does not exist!" % file_path)
    else:
        # return the whole file-path
        return file_path


def _is_valid_file(parser, path):
    file_path = _add_root_path(path)
    if not os.path.exists(file_path):
        parser.error("The file %s does not exist!" % file_path)

    else:
        return file_path


def _is_percentage_number(parser, number):
    if 0 <= int(number) <= 100:
        return number
    else:
        parser.error("Not a correct percentage number")


def _is_positive_int(parser, number):
    if number >= 0 and isinstance(number, int):
        return number
    else:
        parser.error("Not a positive integer")


def _is_non_empty_list(parser, new_list):
    if not isinstance(new_list, list):
        parser.error("The provided parameter is not a list")
    if len(new_list) < 1:
        parser.error("Provided list is empty.")
    else:
        return new_list
