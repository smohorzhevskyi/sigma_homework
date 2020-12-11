"""
Напишите функцию для получения строки из заданной строки, в которой все вхождения ее первого символа заменены на '_'
(нижнее подчеркивание), кроме самого первого символа
Пример строки: 'abracadabra'
Ожидаемый результат: 'abr_c_d_br_'
"""


def replacing_char(string):
    return string[0] + string[1:].replace(string[0], "_")


print("Converted string: ", replacing_char(input('Enter string to convert: ')))
