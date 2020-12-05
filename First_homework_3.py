"""
Вывести символ * построчно, начиная с одной звездочки и, в зависимости от количества строк, заданных пользователем,
последовательно увеличивая на 1 звездочку на каждой новой строке. Если пользователь вводить числа меньшие 1 –
бросить исключение.
"""


def checknum(N):
    if N < 0:
        raise Exception()


N = int(input())
count = 0

try:
    checknum(N)
except Exception as e:
    print('Should be more than 1')
else:
    while count <= N:
        print('*' * count)
        count += 1
