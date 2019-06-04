import sys
from generation.command_line_parser import parse_command_line_evaluator
from moses_file_reader import read_moses_files
from evaluators.accuracy_evaluator import AccuracyEvaluator
from evaluators.chrf_evaluator import ChrfEvaluator


def main():
    args = parse_command_line_evaluator(sys.argv)

    input_files = read_moses_files([args.file_source, args.file_target])

    # evaluation
    accuracy_evaluator = AccuracyEvaluator()
    chrf_evaluator = ChrfEvaluator()

    accuracy_scoring, accuracy = accuracy_evaluator.evaluate(input_files[0], input_files[1])
    chrf_scoring, chrf_score = chrf_evaluator.evaluate(input_files[0], input_files[1])

    scoring_list = ["Accuracy || chrf score \n"]

    for i in range(0, len(accuracy_scoring)):
        scoring_list.append(str(accuracy_scoring[i]) + " || " + str(chrf_scoring[i]) + "\n")

    scoring_list.append("===================================")
    scoring_list.append("Accuracy scoring: " + str(accuracy) + " || " + "Chrf-Score: " + str(chrf_score) + "\n")

    scoring_file = open(args.output, 'w+')
    scoring_file.writelines(scoring_list)
    scoring_file.close()


if __name__ == '__main__':
    main()
