import math


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        # Initialize the numerator and denominator properties
        # Check that the denominator is non-zero
        self.numerator = numerator
        if denominator == 0 and numerator != 0:
            raise ZeroDivisionError
        self.denominator = denominator

    def add(self, other):
        # Add the current fraction and the other fraction
        # Return the result as a new Fraction object
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            resulting_denominator = self.denominator * other.denominator
            resulting_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return Fraction(resulting_numerator, resulting_denominator)

    def subtract(self, other):
        # Subtract the other fraction from the current fraction
        # Return the result as a new Fraction object
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            resulting_denominator = self.denominator * other.denominator
            resulting_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            return Fraction(resulting_numerator, resulting_denominator)

    def multiply(self, other):
        # Multiply the current fraction and the other fraction
        # Return the result as a new Fraction object
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def divide(self, other):
        # Divide the current fraction by the other fraction
        # Check that the other fraction has a non-zero numerator
        # Return the result as a new Fraction object
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def simplify(self):
        # Simplify the current fraction to its simplest form
        # Return a new Fraction object with the simplified numerator and denominator
        if math.gcd(self.numerator, self.denominator) == self.denominator:
            return self.numerator // self.denominator
        elif math.gcd(self.numerator, self.denominator) == 1:
            return Fraction(self.numerator, self.denominator)
        else:
            resulting_numerator = self.numerator // math.gcd(self.numerator, self.denominator)
            resulting_denominator = self.denominator // math.gcd(self.numerator, self.denominator)
            return Fraction(resulting_numerator, resulting_denominator)

    def __str__(self):
        # Return the string representation of the fraction in the format "numerator/denominator"
        return f"{self.numerator}/{self.denominator}"


# Test your implementation
fraction1 = Fraction(1, 4)
fraction2 = Fraction(1, 2)

fraction3 = fraction1.add(fraction2)
print(fraction3)  # Should output "6/8"

fraction4 = fraction3.simplify()
print(fraction4)  # Should output "3/4"
