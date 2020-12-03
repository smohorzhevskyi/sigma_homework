"""
Напишите   функцию,   которая   принимает   2   списка   в   качестве аргументов и возвращает список кортежей,
отсортированный по значению второго элемента в кортеже. Например:
Аргументы:
weekdays = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday','Tuesday', 'Monday']
days = [7, 6, 5, 4, 3, 2, 1].
Функция должна вернуть:
[('Monday',   1),   ('Tuesday',   2),   ('Wednesday',   3),   ('Thursday',   4),('Friday', 5), ('Saturday', 6),
('Sunday', 7)]
"""

weekdays = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
days = [7, 6, 5, 4, 3, 2, 1]
days_of_week = list(zip(weekdays[::-1], sorted(days)))
print(days_of_week)
