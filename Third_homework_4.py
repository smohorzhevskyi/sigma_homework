"""
Напишите  функцию, которая принимает путь к файлу и строку.Внутри функции создайте бинарный файл по заданному адресу и
запишите туда bytearray из полученной строки. Далее необходимо прочитать файл и вернуть список символов исходной строки
в байтовом представлении.
Примерстроки: 'Hello Python'
Ожидаемый результат: [72, 101, 108, 108, 111, 32, 80, 121, 116,104, 111, 110]
"""


def byte_symbols(path, string):
    with open(path, "wb") as f:
        f.write(bytearray(string, "utf-8"))
    with open(path, "rb") as f:
        return [symbol for symbol in f.readline()]


print(byte_symbols(path=r"C:\Users\illia.smohorzhevskyi\Documents\PythonEducation\myfile.txt", string="Hello Python"))
