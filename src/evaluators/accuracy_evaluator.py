import logging
from src.evaluators.evaluator_base import Evaluator


class AccuracyEvaluator(Evaluator):

    def evaluate(self, results: list, targets: list):
        logging.info('Accuracy evaluator: Start evaluating')

        if not isinstance(results, list) or not isinstance(targets, list):
            raise Exception('Parameters provided are not of type `list`.')

        list_length = len(results)
        second_length = len(targets)
        if list_length == 0 or second_length == 0:
            raise Exception('List provided as parameter must not be empty.')

        if list_length != second_length:
            raise Exception('List provided as parameters are not of the same length.')

        scoring = []
        for i in range(0, list_length):
            if results[i] == targets[i]:
                scoring.append(1)
            else:
                scoring.append(0)

        logging.info('Accuracy evaluator: Finished evaluating')
        return scoring
    pass


if __name__ == '__main__':
    print('Subclass:', issubclass(AccuracyEvaluator,
                                  Evaluator))
    print('Instance:', isinstance(AccuracyEvaluator(),
                                  Evaluator))
