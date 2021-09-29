from typing import List
from unittest import TestCase

from simple_array_sum.task import simple_array_sum


class MockTests(TestCase):

    def test_simple_array_sum_1(self) -> None:
        numbers: List[int] = [1, 2, 3, 4, 10, 11]

        self.assertEqual(31, simple_array_sum(numbers))
