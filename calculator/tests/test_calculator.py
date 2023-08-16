import pytest
from app.calculator import Calculator


class TestCalc:
   def setup(self):
       self.calc = Calculator()

   def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(2, 2) == 4

   def test_division_calculate_correctly(self):
       assert self.calc.division(10, 2) == 5

   def test_subtraction_calculate_correctly(self):
       assert self.calc.subtraction(7, 3) == 4

   def test_adding_calculate_correctly(self):
       assert self.calc.adding(5, 3) == 8