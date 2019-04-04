import logging
from src.evaluators.evaluator_base import Evaluator


class AccuracyEvaluator(Evaluator):

    def evaluate(self, results: list, targets: list):
        logging.info('Accuracy evaluator: Start evaluating')
        self._check_params(results, targets)

        scoring = []
        for i in range(0, len(results)):
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
