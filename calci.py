# Imports at top of file
import unittest

# Class definitions

class Calculator:
    """A simple calculator class."""

    def add(self, x_value, y_value):
        """Add two numbers."""
        return x_value + y_value

    def subtract(self, x_value, y_value):
        """Subtract two numbers."""
        return x_value - y_value

    def multiply(self, x_value, y_value):
        """Multiply two numbers."""
        return x_value * y_value

    def divide(self, x_value, y_value):
        """Divide two numbers."""
        if y_value == 0:
            raise ValueError("Division by zero is not allowed")
        return x_value / y_value


class CalculatorTest(unittest.TestCase):
    """Unit tests for the Calculator class."""

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(5, 7), 10, "Addition is wrong")

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(15, 3), 12, "Subtraction is wrong")

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(5, 6), 30, "Multiplication is wrong")

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 2), 3, "Division is wrong")

# Executed only if run as a script    
if __name__ == '__main__':
    unittest.main()