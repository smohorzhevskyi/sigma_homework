"""
1.Создайте класс Calculator который поддерживает:
 сложение двух чисел
 вычисление разницы между двумя числами
 умножение двух чисел
 деление одного числа на другое
 возведение числа в степень
Примеры:
calculator = Calculator()
calculator.add(10,5)➞15
calculator.subtract(10,5)➞5
calculator.multiply(10,5)➞50
calculator.divide(10,5)➞2
calculator.exponent(3, 2) ➞9
"""


class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Can't divide by zero"
        else:
            return x / y

    @staticmethod
    def exponent(x, y):
        return x ** y

