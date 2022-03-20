from unittest import TestCase

from src.trisection import trisection


class Test(TestCase):
    def test_trisection_linear_function(self):
        def linear_function(x): return 2 * x + 1

        expected_solution = -0.5
        self.assertEqual(expected_solution, trisection(-1, 1, linear_function, 0.1))

    def test_trisection_polynomial_function(self):
        def polynomial_function(x): return x ** 3 + 4 * x ** 2 - 10

        expected_solution = 1.3652
        self.assertAlmostEqual(expected_solution, trisection(-2, 2, polynomial_function, 0.0001), 1)