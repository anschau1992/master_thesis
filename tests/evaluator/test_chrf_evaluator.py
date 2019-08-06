import unittest
from src.evaluators.chrf_evaluator import ChrfEvaluator

one_results = ['erweiterten', 'Rechte', 'Symbolisch', 'Verzeichnis', 'führen']
none_results = ['zzz', 'xxx', 'ppp', 'ttt', 'aaa']
almost_targets = ['erweiterten', 'Rechte', 'Symbolischen', 'Verzeichnisse', 'führende']
f_targets = ['erweiterten', 'Rechte', 'Symbolischen', 'Verzeichnisse', 'führende', 'falsche', 'Länge']


class TestChrfEvaluator(unittest.TestCase):

    def setUp(self):
        self.chrfEvaluator = ChrfEvaluator()

    def tearDown(self):
        self.chrfEvaluator = None

    def test_not_list_param(self):
        """
        No list parameter raises an exception
        """
        self.assertRaises(Exception, self.chrfEvaluator.evaluate, 'not a list', one_results, )

    def test_not_same_length(self):
        """
        Not the same length of the two lists raises an exception.
        """
        self.assertRaises(Exception, self.chrfEvaluator.evaluate, one_results, f_targets)

    def test_first_empty_list(self):
        """
        Empty list as first parameter raises an exception.
        """
        self.assertRaises(Exception, self.chrfEvaluator.evaluate, [], f_targets)

    def test_second_empty_list(self):
        """
        Empty list as second parameter raises an exception.
        """
        self.assertRaises(Exception, self.chrfEvaluator.evaluate, one_results, [])

    def test_almost_zero_score(self):
        score = self.chrfEvaluator.evaluate(none_results, one_results)
        self.assertEqual(([1e-16,] * 5, 1.0000000000000001e-16), score, msg='When totally different input, score is almost 0.0')

    def test_one_score(self):
        score = self.chrfEvaluator.evaluate(one_results, one_results)
        self.assertEqual(([1.0] * 5, 1.0), score, msg='When identical entries, the score is 1')

    def test_similiar_high_score(self):
        score = self.chrfEvaluator.evaluate(one_results, almost_targets)
        self.assertEqual(([1.0, 1.0, 0.9803921568627452, 0.9821428571428572, 0.967741935483871],
                          0.9860553898978945), score,
                         msg='When entries are very similiar, score is high')
