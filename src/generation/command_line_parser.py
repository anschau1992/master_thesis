import sys
import logging
import argparse
import os.path
from pathlib import Path

from config import DEFAULT_TRAINING_PATH, DEFAULT_DATA_PATH_DE, DEFAULT_DATA_PATH_EN, \
    DEFAULT_EVAL_SOURCE_PATH, DEFAULT_EVAL_TARGET_PATH

root_path = Path(__file__).parent.parent


def parse_command_line_generator():
    """
    Parse command line argument for the data generation.
     See -h option
    :param argv: arguments on the command line must include caller file name.
    """
    default_data_file_en = str((root_path / DEFAULT_DATA_PATH_EN).resolve())
    default_data_file_de = str((root_path / DEFAULT_DATA_PATH_DE).resolve())
    default_training_file = str((root_path / DEFAULT_TRAINING_PATH).resolve())

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="increase output verbosity (e.g., -vv is more than -v)")
    parser.add_argument("-ien", "--inputEn",
                        dest="file_en", default=default_data_file_en,
                        help="input file with english sentences",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    parser.add_argument("-ide", "--inputDe",
                        dest="file_de", default=default_data_file_de,
                        help="input file with german sentences",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    parser.add_argument("-o", "--output",
                        dest="output", default=default_training_file, help="training data folder location",
                        metavar="DIR",
                        type=lambda x: _check_and_create_folder(x))

    args = parser.parse_args()
    logging.basicConfig(stream=sys.stderr, level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')

    logging.debug('Finished parsing command line arguments for the Generator')
    return args


def parse_command_line_evaluator():
    """
    Parse command line argument for the evaluation
    See -h for options
    :param argv:
    :return:
    """
    default_source_file = str((root_path / DEFAULT_EVAL_SOURCE_PATH).resolve())
    default_target_file = str((root_path / DEFAULT_EVAL_TARGET_PATH).resolve())

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="increase output verbosity (e.g., -vv is more than -v)")
    parser.add_argument("-s", "--source",
                        dest="file_source", default=default_source_file,
                        help="source file with output of the testing phase",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    parser.add_argument("-t", "--target",
                        dest="file_target", default=default_target_file,
                        help="target file with the gold data the model has to predict",
                        metavar="FILE",
                        type=lambda x: _is_valid_file(parser, x))
    args = parser.parse_args()
    logging.basicConfig(stream=sys.stderr, level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')

    logging.debug('Finished parsing command line arguments for the Evaluator')


def _check_and_create_folder(path):
    file_path = str((root_path.parent / path).resolve())
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def _is_valid_file(parser, path):
    if not os.path.exists(path):
        parser.error("The file %s does not exist!" % path)

    else:
        return path  # return the open file handle
