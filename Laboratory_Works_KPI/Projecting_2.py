# Розробити алгоритм і програму дихотомічного пошуку.
# В якості вихідних даних слід використовувати масив цілих чисел,
# який формується за допомогою датчика випадкових чисел з діапазоном від 0 до 100. Аргумент пошуку – число.

from random import randint

N = int(input('Enter the number of elements: '))

while N < 1:
    N = int(input('Wrong! Enter the number of elements again: '))
else:
    array = [randint(0, 100) for element in range(N)]
    array.sort()

X = int(input('Enter the number between 0 and 100: '))

while N < 0 or N > 100:
    X = int(input('Wrong! Enter the number between 0 and 100 again: '))


def binary_search(field, item):
    low = 0
    high = len(field) - 1

    while low <= high:
        mid = (low + high)
        guess = field[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1


if binary_search(array, X) is None:
    print(f"The element {X} in array of {array} is not found")
else:
    print(f"The element {X} in array of {array} is at position of {binary_search(array, X)}")
    print("Remember, that count in Python starts from 0")
