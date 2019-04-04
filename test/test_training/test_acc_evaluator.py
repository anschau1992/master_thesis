import unittest
from src.evaluators.accuracy_evaluator import AccuracyEvaluator

t_results = ['erweiterten', 'Rechte', 'Symbolisch', 'Verzeichnis', 'führen']
none_results = ['erweiter', 'Recht', 'Symbol', 'Verzeichnen', 'führe']
t_targets = ['erweiterten', 'Rechte', 'Symbolischen', 'Verzeichnisse', 'führende']
f_targets = ['erweiterten', 'Rechte', 'Symbolischen', 'Verzeichnisse', 'führende', 'falsche', 'Länge']


class TestAccuracyEvaluator(unittest.TestCase):

    def setUp(self):
        self.accuracyEvaluator = AccuracyEvaluator()

    def tearDown(self):
        self.accuracyEvaluator = None

    def test_not_list_param(self):
        """
        No list parameter raises an exception
        """
        self.assertRaises(Exception, self.accuracyEvaluator.evaluate,  'not a list', t_results,)

    def test_not_same_length(self):
        """
        Not the same length of the two lists raises an exception.
        """
        self.assertRaises(Exception, self.accuracyEvaluator.evaluate, t_results, f_targets)

    def test_first_empty_list(self):
        """
        Empty list as first parameter raises an exception.
        """
        self.assertRaises(Exception, self.accuracyEvaluator.evaluate, [], f_targets)

    def test_second_empty_list(self):
        """
        Empty list as second parameter raises an exception.
        """
        self.assertRaises(Exception, self.accuracyEvaluator.evaluate, t_results, [])

    def test_zero_score(self):
        score = self.accuracyEvaluator.evaluate(none_results, t_targets)
        self.assertEqual(0.0, score, msg='When all results are wrong, score is 0.0')

    def test_correct_accuracy_score(self):
        score = self.accuracyEvaluator.evaluate(t_results, t_targets)
        self.assertEqual(0.4, score, msg='Accuracy-Scoring returned is 0.4')

    def test_not_same_case_accuracy_score(self):
        """
        Same words but wiht not the same case letter are not considered a correct result
        """
        t_results_lowercase = list(map(lambda word: word.lower(), t_results))
        score = self.accuracyEvaluator.evaluate(t_results_lowercase, t_targets)
        self.assertEqual(0.2, score, msg='Accuracy-Scoring when results are all lowercase is 0.2')