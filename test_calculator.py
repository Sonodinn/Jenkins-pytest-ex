import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
    
    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(3, 1) == 2

    def test_multiply(self):
        assert self.calc.multiply(2, 2) == 4

    def test_divide(self):
        assert self.calc.divide(4, 2) == 2

