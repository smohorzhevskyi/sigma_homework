"""
Вывести на печать букву “Z”.
"""

N = 5

print('*' * 7)

for i in range(N):
    print(' ' * N, '*', sep='')
    N -= 1

print('*' * 7)
