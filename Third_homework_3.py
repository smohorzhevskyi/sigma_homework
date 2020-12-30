"""
Напишите  функцию,   которая   принимает   строку   и   возвращает список слов из этой строки,
в которых присутствуют как цифры,так и буквы.Пример строки: 'Dash100 apps are rendered in the web3 browser55'
Ожидаемый результат: ['Dash100', 'web3', 'browser55']
"""


def seeker(string):
    result_list = []
    for word in string.split(' '):
        if any(symbol.isdigit() for symbol in word) and any(symbol.isalpha() for symbol in word):
            result_list.append(word)
    return result_list


print(seeker('Dash100 apps are rendered in the web3 browser55'))

