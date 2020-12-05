"""
Напишите программу для преобразования температуры в градусыЦельсия и Фаренгейта и обратно.
"""

temp = input()


def convertation(temp):
    if temp[-1] == 'F':
        result = round(((float(temp[:-1]) - 32) / 1.8), 2)
        print(temp, 'is', result, sep=' ', end='C')
    elif temp[-1] == 'C':
        result = round(((float(temp[:-1]) * 1.8) + 32), 2)
        print(temp, 'is', result, sep=' ', end='F')


convertation(temp)
