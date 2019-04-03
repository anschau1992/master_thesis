import unittest
from src.evaluators.accuracy_evaluator import AccuracyEvaluator

resultPath = "./test_result"
targetPath = "./test_training"


class TestAccuracyEvaluator(unittest.TestCase):

    def setUp(self):
        self.accuracyEvaluator = AccuracyEvaluator()

    def tearDown(self):
        self.accuracyEvaluator = None

    def test_accuracy_operator(self):
        accuracy = self.accuracyEvaluator.evaluate(resultPath, targetPath)
        self.assertEqual(accuracy, 0.4)
