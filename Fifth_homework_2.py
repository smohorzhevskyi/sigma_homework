"""Напишите декоратор, который сохраняет в log файл название декорируемой функции, ее аргументы и key-word аргументы,
а также считает сколько времени выполнялась декорируемая функция.
Декоратор может быть использован для функций с различным количеством аргументов."""

import logging
import time

logging.basicConfig(filename="logging_my_func.log", level=logging.INFO)


def logger(func):
    def wrapper(*args, **kwargs):
        time_before = time.time()
        result = func(*args, **kwargs)
        logging.info(
            f'Running "{func.__name__}" with arguments {args, kwargs} ran {(time.time() - time_before)} s')
        return result
    return wrapper


@logger
def any_func(*args, **kwargs):
    pass


any_func(6, 7, 8, a=2, b=3)
