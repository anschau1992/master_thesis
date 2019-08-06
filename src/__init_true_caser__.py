import sys
import logging
import os
from pathlib import Path
from generation.true_caser import TrueCaser
from generation.command_line_parser import parse_command_line_true_caser

PREPROCESS_TRUE_CASER = os.environ['PREPROCESS_TRUE_CASER']
TRUE_CASER_COUNT_FILE = os.environ['TRUE_CASER_COUNT_FILE']
DEFAULT_TRAINING_PATH = os.environ['DEFAULT_TRAINING_PATH']

def main():
    args = parse_command_line_true_caser(sys.argv)
    if not PREPROCESS_TRUE_CASER:
        logging.info('True-Caser: is deactivated.')
        sys.exit()
    logging.info('True-Caser: Starting True-caser')

    true_caser = TrueCaser()

    for subdir, dirs, files in os.walk(args.source_data):
        for file in files:
            if '.en' in file:
                logging.info('True_caser: Training true-caser on {0}'.format(os.path.join(subdir, file)))
                with open(os.path.join(subdir, file)) as f:
                    line = f.readline()
                    while line:
                        true_caser.train(line)
                        line = f.readline()
    training_data_path = args.training_data

    if not os.path.exists(training_data_path):
        os.makedirs(training_data_path)
    true_caser.export_counter(training_data_path + TRUE_CASER_COUNT_FILE)


if __name__ == '__main__':
    main()
