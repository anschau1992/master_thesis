import logging
from src.evaluators.evaluator_base import Evaluator
from nltk.translate import chrf_score


class ChrfEvaluator(Evaluator):
    def evaluate(self, results: list, targets: list):
        logging.info('Chrf evaluator: Start evaluating')
        self._check_params(results, targets)

        scoring = list(map(lambda r, t: chrf_score.sentence_chrf(r, t), results, targets))

        logging.info('Chrf evaluator: Finished evaluating')
        return scoring


if __name__ == '__main__':
    print('Subclass:', issubclass(ChrfEvaluator,
                                  Evaluator))
    print('Instance:', isinstance(ChrfEvaluator(),
                                  Evaluator))
