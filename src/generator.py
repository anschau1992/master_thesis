import sys
import argparse
import logging
import os.path
import spacy
from pathlib import Path
from spacy.tokenizer import Tokenizer
from config import TRAIN_SOURCE_FILE_DE, TRAIN_SOURCE_FILE_EN, TRAIN_TARGET_FILE_DE

module = sys.modules['__main__'].__file__
log = logging.getLogger(module)
nlp = spacy.load("de")
tokenizer = Tokenizer(nlp.vocab)

DEFAULT_DATA_PATH_EN = "../data/Ubuntu.de-en.en"
DEFAULT_DATA_PATH_DE = "../data/Ubuntu.de-en.de"
DEFAULT_TRAINING_PATH = "../training"

root_path = Path(__file__).parent

"""
Parse command line argument.
 See -h option
:param argv: arguments on the command line must include caller file name.
"""


def parse_command_line(argv):
    root_path = Path(__file__).parent

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
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-ide", "--inputDe",
                        dest="file_de", default=default_data_file_de,
                        help="input file with german sentences",
                        metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-o", "--output",
                        dest="output", default=default_training_file, help="training data folder location",
                        metavar="DIR",
                        type=lambda x: check_and_create_folder(x))

    args = parser.parse_args()
    logging.basicConfig(stream=sys.stderr, level=(max(3 - args.verbose, 0) * 10),
                        format='%(asctime)s %(levelname)s: %(message)s')

    logging.debug('Finished parsing command line arguments')
    return args


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return the open file handle


def check_and_create_folder(path):
    file_path = str((root_path.parent / path).resolve())
    print(file_path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def read_in_file(fp):
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1


def generate_train_data(fp_en, fp_de, training_path):
    logging.info('Start generate training data')

    line_en = fp_en.readline()
    line_de = fp_de.readline()

    with open(training_path + TRAIN_SOURCE_FILE_EN, "w+") as sourcefile_en:
        with open(training_path + TRAIN_SOURCE_FILE_DE, "w+") as sourcefile_de:
            with open(training_path + TRAIN_TARGET_FILE_DE, "w+") as targetfile_de:
                training_data = []
                while line_en and line_de:
                    tokens = nlp(line_de)
                    for token in tokens:
                        sourcefile_en.write(line_en)

                        lemma = token.lemma_
                        sourcefile_de.write(lemma)
                        if not '\n' in lemma:
                            sourcefile_de.write("\n")
                        targetfile_de.write(str(token))
                        if not '\n' in str(token):
                            targetfile_de.write("\n")

                    line_de = fp_de.readline()
                    line_en = fp_en.readline()

    sourcefile_en.close()
    sourcefile_de.close()
    targetfile_de.close()
    logging.debug('Finish generate training data')


def Main():
    args = parse_command_line(sys.argv)
    generate_train_data(args.file_en, args.file_de, str(args.output))


if __name__ == '__main__':
    Main()
