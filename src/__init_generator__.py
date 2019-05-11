import sys
from generation.command_line_parser import parse_command_line_generator
from moses_file_reader import read_moses_files
from generation.generator import generate_train_data
from generation.validation_test_divider import divide_data

from config import VALIDATION_FRACTION_PERCENTAGE, TEST_FRACTION_PERCENTAGE,\
    TRAIN_SOURCE_FILE_DE, TRAIN_SOURCE_FILE_EN, TRAIN_TARGET_FILE_DE, \
    VAL_SOURCE_FILE_EN, VAL_SOURCE_FILE_DE, VAL_TARGET_FILE_DE,\
    TEST_SOURCE_FILE_EN, TEST_SOURCE_FILE_DE, TEST_TARGET_FILE_DE


def main():
    args = parse_command_line_generator(sys.argv)

    input_files = read_moses_files([args.file_en, args.file_de])

    sources_en, sources_de, targets_de = generate_train_data(input_files[0], input_files[1])

    training_data_set, validation_data_set, test_data_set = \
        divide_data(
            sources_en,
            sources_de,
            targets_de,
            VALIDATION_FRACTION_PERCENTAGE,
            TEST_FRACTION_PERCENTAGE,
        )

    # write training files
    source_file_en = open(args.output + TRAIN_SOURCE_FILE_EN, 'a+')
    source_file_de = open(args.output + TRAIN_SOURCE_FILE_DE, 'a+')
    target_file_de = open(args.output + TRAIN_TARGET_FILE_DE, 'a+')

    source_file_en.writelines(training_data_set.sources_en)
    source_file_de.writelines(training_data_set.sources_de)
    target_file_de.writelines(training_data_set.targets_de)

    source_file_en.close()
    source_file_de.close()
    target_file_de.close()

    # write validation files
    source_file_en = open(args.output + VAL_SOURCE_FILE_EN, 'a+')
    source_file_de = open(args.output + VAL_SOURCE_FILE_DE, 'a+')
    target_file_de = open(args.output + VAL_TARGET_FILE_DE, 'a+')

    source_file_en.writelines(validation_data_set.sources_en)
    source_file_de.writelines(validation_data_set.sources_de)
    target_file_de.writelines(validation_data_set.targets_de)

    source_file_en.close()
    source_file_de.close()
    target_file_de.close()

    # write test files
    source_file_en = open(args.output + TEST_SOURCE_FILE_EN, 'a+')
    source_file_de = open(args.output + TEST_SOURCE_FILE_DE, 'a+')
    target_file_de = open(args.output + TEST_TARGET_FILE_DE, 'a+')

    source_file_en.writelines(test_data_set.sources_en)
    source_file_de.writelines(test_data_set.sources_de)
    target_file_de.writelines(test_data_set.targets_de)

    source_file_en.close()
    source_file_de.close()
    target_file_de.close()


if __name__ == '__main__':
    main()
