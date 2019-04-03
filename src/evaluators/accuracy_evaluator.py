import logging
from src.evaluators.evaluator_base import Evaluator


class AccuracyEvaluator(Evaluator):
    def evaluate(self, resultsPath, targetsPath):
        self._check_proper_files(resultsPath,targetsPath)

        logging.info('Evaluation of Accuracy')

        correct_count = 0
        total_count = 0

        with open(resultsPath + "/result.de", "r") as resultsfile_de:
            with open(targetsPath + "/train.trg.de", "r") as targetsfile_de:

                result = resultsfile_de.readline()
                target = targetsfile_de.readline()

                while result and target:
                    if result == target:
                        correct_count = correct_count + 1
                    total_count = total_count + 1

                    result = resultsfile_de.readline()
                    target = targetsfile_de.readline()

        resultsfile_de.close()
        targetsfile_de.close()
        return correct_count / total_count


if __name__ == '__main__':
    print('Subclass:', issubclass(AccuracyEvaluator,
                                  Evaluator))
    print('Instance:', isinstance(AccuracyEvaluator(),
                                  Evaluator))
