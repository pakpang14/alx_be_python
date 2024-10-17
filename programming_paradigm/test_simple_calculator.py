import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(6, -4), 2)


    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-2, 1), -3)
        self.assertEqual(self.calc.subtract(4, -1), 5)


    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 1), -2)
        self.assertEqual(self.calc.multiply(3, -2), -6)



    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(6, -1), -6)
        self.assertEqual(self.calc.divide(-4, 2), -2)


if __name__ == "__main__":
    unittest.main()