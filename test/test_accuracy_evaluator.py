import unittest
from src.evaluators.accuracy_evaluator import AccuracyEvaluator

resultPath_t = "./test_result"
targetPath_t = "./test_training"

differentLengthPath = "./test_length"


class TestAccuracyEvaluator(unittest.TestCase):

    def setUp(self):
        self.accuracyEvaluator = AccuracyEvaluator()

    def tearDown(self):
        self.accuracyEvaluator = None

    def test_accuracy_operator(self):
        accuracy = self.accuracyEvaluator.evaluate(resultPath_t, targetPath_t)
        self.assertEqual(accuracy, 0.4)

    def test_different_line_length(self):
        self.assertRaises(Exception, self.accuracyEvaluator.evaluate, differentLengthPath, targetPath_t)