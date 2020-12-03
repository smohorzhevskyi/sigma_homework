"""
Напишите функцию, которая принимает список строк в качестве аргумента   и   возвращает   отфильтрованный   список,
который содержит   только   строки,   которые   являются   палиндромами.
Например: Аргументы: words   =   ["radar", "device", "level", "program", "kayak", "river", "racecar"]
Функция должна вернуть : ['radar', 'level', 'kayak', 'racecar']
"""

words = input().split()
filtered_list = filter(lambda i: i == i[::-1], words)
print(list(filtered_list))

"Ниже вариант без использования лямбда-функции"

# words = input().split()
#
#
# def palindrom_search(words, palindrom_list=[]):
#     for i in words:
#         if i == i[::-1]:
#             palindrom_list.append(i)
#     print(palindrom_list)
#
#
# palindrom_search(words)
