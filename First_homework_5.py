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


def correct_input(result):
    user_input = input('Enter 6 cards: ').replace("'", "").split(', ')
    for elem in user_input:
        if elem not in cards:
            user_input = input('Some card was wrong, try again: ').replace("'", "").split(', ')
            continue
        result += significance.get(elem)
    print(result)

correct_input(result)
