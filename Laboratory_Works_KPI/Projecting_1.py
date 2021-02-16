# Скласти програму, яка формує матрицю з n х n випадкових чисел. Визначити
# суму від’ємних чисел і окремо – суму інших. Значення n змінюється в межах від 5
# до 10 тисяч.

from datetime import datetime

S = [1, 3, 5, 6, 7, 8, 9, 10]
A = 0
K = int(input("Input what K-biggest element to find in S: "))

while K < 1 or K > len(S):
    K = int(input(f"K shouldn't be bigger than {len(S)} or less than 1: "))

before = datetime.now()


def k_biggest(array, k):
    array.sort()
    global A
    A = array[-k]
    S.remove(A)
    S.insert(k, A)
    return S


after = datetime.now()
print(f"{(after - before).total_seconds() * 1000} is code exec time in ms")
print(f"{K}-biggest in {k_biggest(S, K)} is {S[K-1]} at position of {S.index(A)} (count from 0)")
