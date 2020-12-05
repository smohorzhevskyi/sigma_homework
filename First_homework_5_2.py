"""
Пользователь вводить 6 карт из списка доступных:2, 3, 4, 5, 6, 7, 8, 9,10, 'J', 'Q', 'K', 'A'.
У каждой карты есть свой "вес": 2, 3, 4, 5, 6 весят +1
                                7, 8, 9 весят 0
                                10, 'J', 'Q', 'K', 'A' весят -1
Задача: имея список карт, введенных пользователем посчитать их общий “вес” и вывести результат на печать.
"""

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
significance = {}
result = 0

for card in cards:
    if cards.index(card) >= 8:
        significance[card] = -1
    elif cards.index(card) >= 5:
        significance[card] = 0
    else:
        significance[card] = 1

user_input = input().replace("'", "").split(', ')


def foo(user_input):
    for elem in user_input:
        if elem not in cards:
            raise Exception


try:
    foo(user_input)
except Exception as e:
    print('No card exists!')
else:
    for card in user_input:
        result += significance.get(card)
    print(result)
