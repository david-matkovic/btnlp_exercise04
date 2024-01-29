"""This module provides a simple calculator implementation."""


class Calculator:
    """This class offers basic arithmetic operations."""

    def addition(self, a, b):
        """Add two numbers and return the result.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The sum of a and b.
        """
        return a + b

    def subtraction(self, a, b):
        """Subtract the second number from the first and return the result.

        Parameters:
        a (int): The first number.
        b (int): The number to subtract from the first number.

        Returns:
        int: The difference of a and b.
        """
        return a - b

    def division(self, a, b):
        """Divide the first number by the second and return the result.

        Parameters:
        a (int): The numerator.
        b (int): The denominator; must not be zero.

        Returns:
        float: The quotient of a and b.

        Raises:
        ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    def multiplication(self, a, b):
        """Multiply two numbers and return the result.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The product of a and b.
        """
        return a * b


class Special(Calculator):
    """This class inherits from Calculator and adds modulo and exponential operations."""

    def modulo(self, a, b):
        """Return the remainder of the division of the first number by the second.

        Parameters:
        a (int): The first number (dividend).
        b (int): The second number (divisor).

        Returns:
        int: The remainder of a divided by b.
        """
        return a % b

    def exponential(self, a, b):
        """Raise the first number to the power of the second and return the result.

        Parameters:
        a (int): The base number.
        b (int): The exponent.

        Returns:
        int: The result of a raised to the power of b.
        """
        return a ** b


# Example usage:
calc = Special()
print(calc.addition(10, 5))
print(calc.subtraction(10, 5))
print(calc.multiplication(10, 5))
print(calc.division(10, 5))
print(calc.modulo(10, 5))
print(calc.exponential(10, 5))
