import argparse
import os.path
import nltk
from nltk.tokenize import word_tokenizepi
from germalemma import GermaLemma

#lemmatizer = WordNetLemmatizer()
lemmatizer = GermaLemma()
german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
nltk.download('punkt')
nltk.download('wordnet')


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


def generate_train_data(fp_en, fp_de):
    line_en = fp_en.readline()
    line_de = fp_de.readline()

    training_data = []
    while line_en and line_de:
        tokens = word_tokenize(line_de)
        #tokens = german_tokenizer(line_de)
        for token in tokens:
            print(token + ": " + lemmatizer.find_lemma(token))
        line_de = fp_de.readline()
        line_en = fp_en.readline()


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ien", "--inputEn",
                        dest="file_en", default=EN_FILE_PATH, help="input file with english sentences", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-ide", "--inputDe",
                        dest="file_de", default=DE_FILE_PATH, help="input file with german sentences", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()
    # read_in_file(args.file_de)
    generate_train_data(args.file_en, args.file_de)


if __name__ == '__main__':
    Main()
