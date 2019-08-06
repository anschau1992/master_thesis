import sys
import os
import logging
from collections import Counter
from generation.command_line_parser import parse_scoring_no_most_common

# read configs
MOST_COMMON_NUMBER = int(os.environ["MOST_COMMON_NUMBER"])
TEST_SOURCE_FILE_EN = os.environ["TEST_SOURCE_FILE_EN"]
TEST_SOURCE_FILE_DE = os.environ["TEST_SOURCE_FILE_DE"]
TEST_TARGET_FILE_DE = os.environ["TEST_TARGET_FILE_DE"]
TEST_BASE_FILE_DE = os.environ["TEST_BASE_FILE_DE"]
TEST_OUTPUT_FILE_DE = os.environ["TEST_OUTPUT_FILE_DE"]


def main():
    args = parse_scoring_no_most_common(sys.argv)

    logging.info('** Start of scoring No-Most-Common **')

    most_common_de = initialize_most_common(args.de_file)

    input_path = args.input
    output_path = args.output
    with open(input_path + TEST_BASE_FILE_DE) as bases_de, \
            open(input_path + TEST_TARGET_FILE_DE) as targets_de, \
            open(input_path + TEST_SOURCE_FILE_DE) as sources_de, \
            open(input_path + TEST_SOURCE_FILE_EN) as sources_en, \
            open(input_path + TEST_OUTPUT_FILE_DE) as outputs_de, \
            open(output_path + TEST_BASE_FILE_DE, 'w+') as output_base_de, \
            open(output_path + TEST_TARGET_FILE_DE, 'w+') as output_target_de, \
            open(output_path + TEST_SOURCE_FILE_DE, 'w+') as output_source_de, \
            open(output_path + TEST_SOURCE_FILE_EN, 'w+') as output_source_en, \
            open(output_path + TEST_OUTPUT_FILE_DE, 'w+') as output_outputs_de:

        for source_de in sources_de:
            target_de = next(targets_de).strip()
            source_en = next(sources_en).strip()
            base_de = next(bases_de).strip()
            output_de = next(outputs_de).strip()

            if most_common_de[source_de.rstrip()] == 0:
                output_base_de.write(__assure_line_break(base_de))
                output_target_de.write(__assure_line_break(target_de))
                output_source_de.write(__assure_line_break(source_de))
                output_source_en.write(__assure_line_break(source_en))
                output_outputs_de.write(__assure_line_break(output_de))


def initialize_most_common(file):
    with open(file) as f:
        most_common = Counter()
        line_count = 1
        for line in f:
            if line_count >= MOST_COMMON_NUMBER:
                break
            most_common[line.rstrip()] = -line_count
            line_count += 1
        return most_common


def __assure_line_break(line):
    if not '\n' in line:
        return line + '\n'
    return line


if __name__ == '__main__':
    main()
