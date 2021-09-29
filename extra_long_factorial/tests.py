from unittest import TestCase

from extra_long_factorial.task import extra_long_factorials


class ExtraLongFactorialTest(TestCase):

    def test_extra_long_factorial_1(self):
        self.assertEqual(15511210043330985984000000, extra_long_factorials(25))
