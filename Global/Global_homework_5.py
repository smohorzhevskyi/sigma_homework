import time
import threading
import random


# Під час запуску цього файлу створюється додатковий потік,
# який заповнює файл rec.data випадковими числовими данними.
# Необхідно створити рекурсивну функцію, яка буде повертати останнє число з файлу
# та показувати його під час читання файла.
# Початковий період читання данних з файлу має 0 інтервал,
# Після отримання данних з файлу має бути замінений на останнє число з файлу.
# Час роботи функції потрібно обмежити до 60 секунд.
# Додатковий потік працює доти, поки працює рекурсивна функція

# def rec_function(timer=10):
#     print(1)
#     # time.sleep(period)
#     if timer != 0:
#         return None
#     rec_function(timer-1)
#     return 1


def run(period, inc=0):
    print("Hello user, time left:", period)
    inc += 0.5
    time.sleep(0.5)
    if period <= 0:
        return None
    run(period-inc, inc)
    return 1


run(10)


# def random_data(filepath):
#     time.sleep(random.random())
#     with open(filepath, 'a') as file:
#         file.write(f"{random.randint(0, 7)}")
#     random_data(filepath)
#
#
# def main():
#     data_thread = threading.Thread(target=random_data, args=('rec.data',), daemon=True)
#     data_thread.start()
#     rec_function(1, 1)  # recursion function call
#     time.sleep(10)  # delete after creation your function
#     print("Application Exit")
#
#
# main()
