import unittest
from typing import List

from compare_the_triplets.task import compare_triplets


class MyTestCase(unittest.TestCase):

    def test_compare_triplets_1(self):
        alices_points: List[int] = [17, 28, 30]
        bobs_points: List[int] = [99, 16, 8]

        self.assertEqual((2, 1), compare_triplets(alices_points, bobs_points))

    def test_compare_triplets_2(self):
        alices_points: List[int] = [99, 16, 8]
        bobs_points: List[int] = [17, 28, 30]

        self.assertEqual((1, 2), compare_triplets(alices_points, bobs_points))

    def test_compare_triplets_3(self):
        alices_points: List[int] = [17, 28, 30]
        bobs_points: List[int] = [99, 28, 8]

        self.assertEqual((1, 1), compare_triplets(alices_points, bobs_points))
