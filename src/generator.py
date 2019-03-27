import argparse
import logging
import os.path
import spacy
from spacy.tokenizer import Tokenizer
from trainingEntry import TrainingEntry

nlp = spacy.load("de")
tokenizer = Tokenizer(nlp.vocab)

EN_FILE_PATH = "./data/Ubuntu.de-en.en"
DE_FILE_PATH = "./data/Ubuntu.de-en.de"


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return the open file handle


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




# def write_training_data_out(training_data, fp):
#     print('Writing data')
#     with open(fp + "/train.src.en", "a+") as sourcefile_en:
#         with open(fp + "/train.src.de", "a+") as sourcefile_de:
#             with
#     targetfile_de = open(fp + "/train.trg.de", "w+")
#
#     for entry in training_data:
#         sourcefile_en.write(entry.sentence)
#         sourcefile_de.write(entry.token)
#         targetfile_de.write(entry.lemma)
#
#     sourcefile_en.close()
#     sourcefile_de.close()
#     targetfile_de.close()
#     print('FInished')


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ien", "--inputEn",
                        dest="file_en", default=EN_FILE_PATH, help="input file with english sentences", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-ide", "--inputDe",
                        dest="file_de", default=DE_FILE_PATH, help="input file with german sentences", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()
    #read_in_file(args.file_de)

    training_data = generate_train_data(args.file_en, args.file_de, './training')

if __name__ == '__main__':
    Main()
