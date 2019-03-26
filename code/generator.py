import argparse
import os.path

EN_FILE_PATH = "./data/Ubuntu.de-en.en"
DE_FILE_PATH = "./data/Ubuntu.de-en.de"

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return the open file handle


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ien", "--inputEn",
                        dest="file_en", default=EN_FILE_PATH, help="input file with english sentences", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-ide", "--inputDe",
                        dest="file_de", default=DE_FILE_PATH, help="input file with german sentences", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()
    print("Filepath EN " + str(args.file_en))
    print("Filepath DE " + str(args.file_de))


if __name__ == '__main__':
    Main()
