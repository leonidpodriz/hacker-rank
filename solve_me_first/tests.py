from unittest import TestCase
from unittest.mock import MagicMock, patch

from solve_me_first.task import solve_me_first


class SolveMeFirstTest(TestCase):

    def test_function_1(self) -> None:
        self.assertEqual(5, solve_me_first(2, 3))

    def test_function_2(self) -> None:
        self.assertEqual(10, solve_me_first(4, 6))

    @patch('builtins.sum', return_value=10)
    def test_function_3_with_mock_example(self, mocked_sum: MagicMock) -> None:
        self.assertEqual(0, mocked_sum.call_count)
        self.assertEqual(10, solve_me_first(4, 6))
        self.assertEqual(1, mocked_sum.call_count)
        mocked_sum.assert_called_once_with((4, 6))
