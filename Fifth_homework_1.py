"""Напишите декоратор, который считает сколько раз была вызвана декорируемая функция.
Декоратор может быть использован для функций с различным количеством аргументов.
"""
COUNTER = 0


def my_decorator(foo_to_decorate):
    def wrapper(*args, **kwargs):
        global COUNTER
        time = 'times' if COUNTER > 1 else 'time'
        COUNTER += 1
        print(f"This function was called {COUNTER} {time}")
        return foo_to_decorate(*args, **kwargs)
    return wrapper


@my_decorator
def any_func(*args, **kwargs):
    pass

