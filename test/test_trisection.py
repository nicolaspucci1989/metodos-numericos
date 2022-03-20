from unittest import TestCase

from src.trisection import trisection


class Test(TestCase):
    def test_trisection_linear_function(self):
        def linear_function(x): return 2 * x + 1

        expected_solution = -0.5
        self.assertEqual(expected_solution, trisection(-1, 1, linear_function, 0.1))
