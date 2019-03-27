import argparse
import logging
import os.path
import spacy
from spacy.tokenizer import Tokenizer

nlp = spacy.load("de")
tokenizer = Tokenizer(nlp.vocab)

DEFAULT_DATA_PATH_EN = "./data/Ubuntu.de-en.en"
DEFAULT_DATA_PATH_DE = "./data/Ubuntu.de-en.de"
DEFAULT_TRAINING_PATH = "./training"


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return the open file handle


def check_and_create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def read_in_file(fp):
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1


def generate_train_data(fp_en, fp_de, training_path):
    print('Start generating data')
    line_en = fp_en.readline()
    line_de = fp_de.readline()

    with open(training_path + "/train.src.en", "w+") as sourcefile_en:
        with open(training_path + "/train.src.de", "w+") as sourcefile_de:
            with open(training_path + "/train.trg.de", "w+") as targetfile_de:
                training_data = []
                while line_en and line_de:
                    tokens = nlp(line_de)
                    for token in tokens:
                        sourcefile_en.write(line_en)
                        sourcefile_en.write("\n")
                        sourcefile_de.write(token.lemma_)
                        sourcefile_de.write("\n")
                        targetfile_de.write(str(token))
                        targetfile_de.write("\n")

                    line_de = fp_de.readline()
                    line_en = fp_en.readline()

    sourcefile_en.close()
    sourcefile_de.close()
    targetfile_de.close()


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ien", "--inputEn",
                        dest="file_en", default=DEFAULT_DATA_PATH_EN, help="input file with english sentences",
                        metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-ide", "--inputDe",
                        dest="file_de", default=DEFAULT_DATA_PATH_DE, help="input file with german sentences",
                        metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-o", "--output",
                        dest="output", default=DEFAULT_TRAINING_PATH, help="training data folder location",
                        metavar="DIR",
                        type=lambda x: check_and_create_folder(x))
    args = parser.parse_args()

    generate_train_data(args.file_en, args.file_de, str(args.output))


if __name__ == '__main__':
    Main()
