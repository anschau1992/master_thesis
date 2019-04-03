from abc import ABC, abstractmethod



class Evaluator(ABC):

    @abstractmethod
    def evaluate(self, resultsPath, targetsPath):
        pass
        """
        Evaluates the scoring of the NMT.
        :param resultsPath: file path to the results file
        :param targetsPath: file path to the targets (gold) file
        :return: scoring value
        """
