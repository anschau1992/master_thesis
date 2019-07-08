import sys
import logging
from generation.command_line_parser import parse_command_line_generator
from moses_file_reader import MosesFileReader
from generation.generator import generate_train_data
from generation.validation_test_divider import ValidationTestDivider

from config import VALIDATION_FRACTION_PERCENTAGE, TEST_FRACTION_PERCENTAGE, \
    TRAIN_SOURCE_FILE_DE, TRAIN_SOURCE_FILE_EN, TRAIN_TARGET_FILE_DE, \
    VAL_SOURCE_FILE_EN, VAL_SOURCE_FILE_DE, VAL_TARGET_FILE_DE, \
    TEST_SOURCE_FILE_EN, TEST_SOURCE_FILE_DE, TEST_TARGET_FILE_DE, \
    TRAIN_BASE_FILE_DE, VAL_BASE_FILE_DE, TEST_BASE_FILE_DE


def main():
    args = parse_command_line_generator(sys.argv)

    print(args.perValid)
    print(args.perTest)

    validation_percentage = VALIDATION_FRACTION_PERCENTAGE
    test_percentage = TEST_FRACTION_PERCENTAGE

    if args.perValid is not None:
        validation_percentage = float(args.perValid)

    if args.perTest is not None:
        test_percentage = float(args.perTest)

    logging.info("Open up data file for writing generated data into it.")
    train_source_file_en = open(args.output + TRAIN_SOURCE_FILE_EN, 'a+')
    train_source_file_de = open(args.output + TRAIN_SOURCE_FILE_DE, 'a+')
    train_target_file_de = open(args.output + TRAIN_TARGET_FILE_DE, 'a+')
    train_base_file_de = open(args.output + TRAIN_BASE_FILE_DE, 'a+')

    val_source_file_en = open(args.output + VAL_SOURCE_FILE_EN, 'a+')
    val_source_file_de = open(args.output + VAL_SOURCE_FILE_DE, 'a+')
    val_target_file_de = open(args.output + VAL_TARGET_FILE_DE, 'a+')
    val_base_file_de = open(args.output + VAL_BASE_FILE_DE, 'a+')

    test_source_file_en = open(args.output + TEST_SOURCE_FILE_EN, 'a+')
    test_source_file_de = open(args.output + TEST_SOURCE_FILE_DE, 'a+')
    test_target_file_de = open(args.output + TEST_TARGET_FILE_DE, 'a+')
    test_base_file_de = open(args.output + TEST_BASE_FILE_DE, 'a+')

    moses_file_reader = MosesFileReader([args.file_en, args.file_de])
    val_test_divider = ValidationTestDivider(validation_percentage, test_percentage)

    while True:
        # generate train_data with it
        next_lines = moses_file_reader.read_next_lines()

        if next_lines is None:
            break

        sources_en, sources_de, targets_de, base_de = generate_train_data(next_lines[0], next_lines[1])
        training_data_set, validation_data_set, test_data_set = val_test_divider.divide_data(sources_en, sources_de,
                                                                                             targets_de, base_de)
        train_source_file_en.writelines(training_data_set.sources_en)
        train_source_file_de.writelines(training_data_set.sources_de)
        train_target_file_de.writelines(training_data_set.targets_de)
        train_base_file_de.writelines(training_data_set.base_de)

        val_source_file_en.writelines(validation_data_set.sources_en)
        val_source_file_de.writelines(validation_data_set.sources_de)
        val_target_file_de.writelines(validation_data_set.targets_de)
        val_base_file_de.writelines(validation_data_set.base_de)

        test_source_file_en.writelines(test_data_set.sources_en)
        test_source_file_de.writelines(test_data_set.sources_de)
        test_target_file_de.writelines(test_data_set.targets_de)
        test_base_file_de.writelines(test_data_set.base_de)

    train_source_file_en.close()
    train_source_file_de.close()
    train_target_file_de.close()
    train_base_file_de.close()

    val_source_file_en.close()
    val_source_file_de.close()
    val_target_file_de.close()
    val_base_file_de.close()

    test_source_file_en.close()
    test_source_file_de.close()
    test_target_file_de.close()
    test_base_file_de.close()

    logging.info('Generator - Generate {0} lines of data. Train: {1}; Val: {2}; Test: {3}; Ratio: {4}/{5}/{6}'
                 .format(val_test_divider.get_total_count(), val_test_divider.get_train_count(),
                         val_test_divider.get_val_count(), val_test_divider.get_test_count(),
                         (1.00 - val_test_divider.get_validation_ratio() - val_test_divider.get_test_ratio()),
                         val_test_divider.get_validation_ratio(),
                         val_test_divider.get_test_ratio()
                         )
                 )


if __name__ == '__main__':
    main()
