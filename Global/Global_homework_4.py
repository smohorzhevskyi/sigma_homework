"""
Необхідно написати функцію яка буде мати один параметр - один рядок з файлу incoming_log
Якщо аргумент функції буде мати "Failed to decode",
то потрібно буде з вхідного рядка отримати базове імя файлу, та записати його в файл failed.txt.
Всі інші рядки просто пропустити.
Функція має повертати список імен всіх знайдених шляхів файлів, що долучались в failed.txt.
"""

import os


def mining(string, cache=[]):
    if "Failed to decode" in string and string.find(".") != -1:
        if "/" in string:
            with open("failed.txt", "a+") as f:
                result_line = string.split('/')[-1]
                f.write(result_line)
                cache.append(os.path.splitext(string.split()[-1])[0])
    return cache


with open("incoming_log.txt", "r") as log:
    for s in log.readlines():
        result = mining(s)

print(result)
