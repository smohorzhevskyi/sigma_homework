"""Задание 3 (Python)
Напишите программу, рассчи
Задание 3 (Python)
Напишите программу, рассчитывающую факториал
Например, входящее значение:
8
Вывод на экран:
40320"""

from functools import reduce

N = int(input("Enter N: "))

number_list = [i for i in range(1, N+1)]

result = reduce(lambda x, y: x * y, number_list) if N != 0 else 1

print(result)
