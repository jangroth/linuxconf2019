from unittest import TestCase

from code.classes import Calculator


class TestCalculator(TestCase):

    def test_multiply_with_zero_is_zero(self):
        # setup
        calc = Calculator(29)

        # exercise
        result = calc.multiply_by(0)

        # verify
        self.assertEqual(0, result)
