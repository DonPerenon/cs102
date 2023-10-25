import unittest
import tkinter as tk
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab1.calculator import Calculator

sys.path.append('/Users/viktorivanov/cs102/src')
from lab1.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):


    def test_addition(self):
        calculator = Calculator(tk.Tk())
        calculator.button_8.invoke()
        calculator.add_button.invoke()
        calculator.button_7.invoke()
        calculator.equal_button.invoke()
        answer = calculator.number_entry.get()
        self.assertEqual(answer, "15")


    def test_substruction(self):
        calculator = Calculator(tk.Tk())
        calculator.button_3.invoke()
        calculator.subtract_button.invoke()
        calculator.button_6.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "-3")


    def test_multiplication(self):
        calculator = Calculator(tk.Tk())
        calculator.button_3.invoke()
        calculator.multiply_button.invoke()
        calculator.button_7.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "21")


    def test_division(self):
        calculator = Calculator(tk.Tk())
        calculator.button_9.invoke()
        calculator.divide_button.invoke()
        calculator.button_3.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "3.0")


    def test_floor_division(self):
        calculator = Calculator(tk.Tk())
        calculator.button_7.invoke()
        calculator.floor_div_button.invoke()
        calculator.button_2.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "3")


    def test_moduling(self):
        calculator = Calculator(tk.Tk())
        calculator.button_6.invoke()
        calculator.modulus_button.invoke()
        calculator.button_4.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "2")


    def test_root_calculation(self):
        calculator = Calculator(tk.Tk())
        calculator.button_9.invoke()
        calculator.sqrt_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "3")

