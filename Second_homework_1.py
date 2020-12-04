"""
Напишите lambda функцию, которая принимает два аргумента x и y и возвращает результат деления x на y
при условии, что делитель не равен 0, иначе возвращаем None.
"""
x, y = [int(i) for i in input().split()]
result = lambda x, y: x / y

try:
    print(result(x, y))
except (ZeroDivisionError, ValueError):
    print("None")


"Это не совсем по PEP8 - потому я переписал ниже"

# x, y = [int(i) for i in input().split()]
# def division(*args): return x / y
#
#
# try:
#     print(division(x, y))
# except (ZeroDivisionError, ValueError):
#     print("None")
