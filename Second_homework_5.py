"""
Напишите рекурсивную функцию, которая возвращает сумму всех элементов   в   списке   целых   чисел.
Функция   должна   уметь обрабатывать в том числе и вложенные списки,
например такие как - [1, 2, [3,4], [5,6, [7,8,9,10]]]
"""

elements = [1, 2, [3, 4], [5, 6, [7, 8, 9, 10]]]


def recursion(listing, total=0):
    for number in listing:
        if type(number) is list:
            total += recursion(number)
        else:
            total += number
    return total


print(recursion(elements))
