from sys import maxsize
from random import randint
from datetime import datetime

before = datetime.now()
n = randint(5000, 10000)
positive_sum, negative_sum = 0, 0
array = [[randint(-maxsize, maxsize)] * n for element in range(n)]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] < 0:
            negative_sum += array[i][j]
        else:
            positive_sum += array[i][j]


after = datetime.now()
print("Розмір матриці: ", n, 'x', n, sep='')
print("Сума додатніх чисел: ", positive_sum)
print("Сума від'ємних чисел: ", negative_sum)
print("Витрачено часу: ", after - before)
