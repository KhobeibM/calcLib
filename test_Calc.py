"""
Unit tests for the calculator library
"""

import Calc


class TestCalculator:

    def test_addition(self):
        assert 4 == Calc.add(2, 2)

    def test_subtraction(self):
        assert 2 == Calc.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == Calc.multiply(10, 10)
