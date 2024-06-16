
from math import gcd
 
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        self.numerator = numerator
        self.denominator = denominator
 
    def add(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
 
    def subtract(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
 
    def multiply(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
 
    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by a fraction with a zero numerator.")
        
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)
 
    def simplify(self):
        greatest_common_divisor = gcd(self.numerator, self.denominator)
        simplified_numerator = self.numerator // greatest_common_divisor
        simplified_denominator = self.denominator // greatest_common_divisor
        return Fraction(simplified_numerator, simplified_denominator)
 
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"