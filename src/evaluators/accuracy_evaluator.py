import logging
from evaluators.evaluator_base import Evaluator


class AccuracyEvaluator(Evaluator):


    def evaluate(self, results: list, targets: list):
        logging.info('Accuracy evaluator: Start evaluating')
        self._check_params(results, targets)

        scoring = []

        result_length = len(results)
        correct = 0
        for i in range(0, result_length):
            if results[i] == targets[i]:
                scoring.append(1)
                correct += 1
            else:
                scoring.append(0)

        logging.info('Accuracy evaluator: Finished evaluating')
        return scoring, (correct/result_length)
    pass


if __name__ == '__main__':
    print('Subclass:', issubclass(AccuracyEvaluator,
                                  Evaluator))
    print('Instance:', isinstance(AccuracyEvaluator(),
                                  Evaluator))
