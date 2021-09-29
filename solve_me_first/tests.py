from unittest import TestCase

from solve_me_first.task import solve_me_first


class SolveMeFirstTest(TestCase):

    def test_function_1(self):
        self.assertEqual(solve_me_first(2, 3), 5)

    def test_function_2(self):
        self.assertEqual(solve_me_first(4, 6), 10)
