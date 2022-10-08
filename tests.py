import unittest
from calc import calculate

class TestCalculator(unittest.TestCase):

    def test_calculate(self):
        assert calculate("0+11") == 11
        assert calculate("11+1-3") == 9
        assert calculate("11*2") == 22
        assert calculate("12435+34569-12345*10+50") == eval("12435+34569-12345*10+50")