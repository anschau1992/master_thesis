import sys
import os
import logging
from sampling.undersampler import undersample_data

from generation.command_line_parser import parse_sampling

# read configs
TRAIN_SOURCE_FILE_EN = os.environ["TRAIN_SOURCE_FILE_EN"]
TRAIN_SOURCE_FILE_DE = os.environ["TRAIN_SOURCE_FILE_DE"]
TRAIN_TARGET_FILE_DE = os.environ["TRAIN_TARGET_FILE_DE"]
TRAIN_BASE_FILE_DE = os.environ["TRAIN_BASE_FILE_DE"]
TRAIN_POS_FILE_DE = os.environ["TRAIN_POS_FILE_DE"]


def main():
    logging.info("Start undersampling")
    args = parse_sampling(sys.argv)
    dirpath = args.path
    print(dirpath)

    with open(dirpath + TRAIN_SOURCE_FILE_EN) as source_file_en, \
            open(dirpath + TRAIN_SOURCE_FILE_DE) as source_file_de, \
            open(dirpath + TRAIN_TARGET_FILE_DE) as target_file_de, \
            open(dirpath + TRAIN_BASE_FILE_DE) as base_file_de, \
            open(dirpath + TRAIN_POS_FILE_DE) as pos_file_de:
        logging.info("Opened up data file for undersampling.")
        undersample_data(source_file_en, source_file_de, target_file_de, base_file_de, pos_file_de, dirpath)
        logging.info("Fnished undersampling.")


if __name__ == '__main__':
    main()
