import sys
from generation.command_line_parser import parse_command_line
from moses_file_reader import read_moses_files
from generation.generator import generate_train_data

from config import TRAIN_SOURCE_FILE_DE, TRAIN_SOURCE_FILE_EN, TRAIN_TARGET_FILE_DE


def main():
    args = parse_command_line(sys.argv)

    input_files = read_moses_files([args.file_en, args.file_de])

    sources_en, sources_de, targets_de = generate_train_data(input_files[0], input_files[1])
    source_file_en = open(args.output + TRAIN_SOURCE_FILE_EN, 'a+')
    source_file_de = open(args.output + TRAIN_SOURCE_FILE_DE, 'a+')
    target_file_de = open(args.output + TRAIN_TARGET_FILE_DE, 'a+')

    source_file_en.writelines(sources_en)
    source_file_de.writelines(sources_de)
    target_file_de.writelines(targets_de)

    source_file_en.close()
    source_file_de.close()
    target_file_de.close()


if __name__ == '__main__':
    main()
