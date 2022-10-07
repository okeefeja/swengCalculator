import unittest
from calc import calculate

class TestCalculator(unittest.TestCase):

    def test_calculate(self):
        assert calculate("12435+34569-12345*10+50") == eval("12435+34569-12345*10+50")

        assert calculate("80*6-4+40*-1") == eval("80*6-4+40*-1")

        assert calculate(5) == 5

