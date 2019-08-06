import sys
import logging
from generation.command_line_parser import parse_scoring_pos_scoring
from config import TEST_SOURCE_FILE_EN, TEST_SOURCE_FILE_DE, TEST_TARGET_FILE_DE, \
    TEST_BASE_FILE_DE, TEST_OUTPUT_FILE_DE, TEST_POS_FILE_DE, DEFAULT_POS_LIST


def main():
    args = parse_scoring_pos_scoring(sys.argv)
    logging.info('** Start of scoring with only specific POS **')

    input_path = args.input
    output_path = args.output
    pos_list = DEFAULT_POS_LIST

    with open(input_path + TEST_BASE_FILE_DE) as bases_de, \
            open(input_path + TEST_TARGET_FILE_DE) as targets_de, \
            open(input_path + TEST_SOURCE_FILE_DE) as sources_de, \
            open(input_path + TEST_SOURCE_FILE_EN) as sources_en, \
            open(input_path + TEST_OUTPUT_FILE_DE) as outputs_de, \
            open(input_path + TEST_POS_FILE_DE) as poss_de, \
            open(output_path + TEST_BASE_FILE_DE, 'w+') as output_base_de, \
            open(output_path + TEST_TARGET_FILE_DE, 'w+') as output_target_de, \
            open(output_path + TEST_SOURCE_FILE_DE, 'w+') as output_source_de, \
            open(output_path + TEST_SOURCE_FILE_EN, 'w+') as output_source_en, \
            open(output_path + TEST_POS_FILE_DE, 'w+') as output_pos_en, \
            open(output_path + TEST_OUTPUT_FILE_DE, 'w+') as output_outputs_de:
        for pos in poss_de:
            target_de = next(targets_de).strip()
            source_de = next(sources_de).strip()
            source_en = next(sources_en).strip()
            base_de = next(bases_de).strip()
            output_de = next(outputs_de).strip()

            if pos.rstrip() in pos_list:
                output_base_de.write(__assure_line_break(base_de))
                output_target_de.write(__assure_line_break(target_de))
                output_source_de.write(__assure_line_break(source_de))
                output_source_en.write(__assure_line_break(source_en))
                output_outputs_de.write(__assure_line_break(output_de))
                output_pos_en.write(__assure_line_break(pos))


def __assure_line_break(line):
    if not '\n' in line:
        return line + '\n'
    return line


if __name__ == '__main__':
    main()
