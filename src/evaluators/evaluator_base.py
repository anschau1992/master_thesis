from abc import ABC, abstractmethod


class Evaluator(ABC):

    @abstractmethod
    def evaluate(self, results: list, targets: list) -> list:
        """
        Evalutes the results compared to the target
        :param results: NMT results
        :param targets: gold results
        :return: the evaluated scores in a list
        """
        pass

    def _check_params(self, results: list, targets: list):
        """
        Base checking for correct parameter input, used in all derived classes.
        It checks:
         - correct type (lists)
         - equal length of lists
         - no empty lists
        :param results:
        :param targets:
        :return:
        """
        if not isinstance(results, list) or not isinstance(targets, list):
            raise Exception('Parameters provided are not of type `list`.')

        list_length = len(results)
        second_length = len(targets)
        if list_length == 0 or second_length == 0:
            raise Exception('List provided as parameter must not be empty.')

        if list_length != second_length:
            raise Exception('List provided as parameters are not of the same length.')