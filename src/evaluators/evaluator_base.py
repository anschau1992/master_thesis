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
