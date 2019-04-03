from abc import ABC, abstractmethod
from src.config import TRAIN_SOURCE_FILE_EN, \
    TRAIN_SOURCE_FILE_DE, \
    TRAIN_TARGET_FILE_DE, \
    RESULT_FILE_DE


class Evaluator(ABC):

    @staticmethod
    def _check_proper_files(resultsPath, targetsPath):
        rpFile = resultsPath + RESULT_FILE_DE
        tpFile = targetsPath + TRAIN_TARGET_FILE_DE


        try:
            rp = open(rpFile, 'r')
            rp_line_count = len(rp.readlines())
            rp.close()
        except FileNotFoundError:
            raise Exception('Result file with path:  {resultsPath} does not exist')

        try:
            tp = open(tpFile, 'r')
            tp_line_count = len(tp.readlines())
            tp.close()
        except FileNotFoundError:
            raise Exception('Target file path: {targetsPath} does not exist')

        if rp_line_count != tp_line_count:
            raise Exception('The line number of the two files are not identical')

    pass

    @abstractmethod
    def evaluate(self, resultsPath, targetsPath):
        pass
        """
        Evaluates the scoring of the NMT.
        :param resultsPath: file path to the results file
        :param targetsPath: file path to the targets (gold) file
        :return: scoring value
        """
