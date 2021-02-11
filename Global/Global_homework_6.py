"""Нужно написать класс который будет создавать объект этого же класса если в конструкторе будет присутствовать
 str "А" или "В" но не что либо другое.
Если в конструктор передается "С" или с "В" также передается "С" то должен быть создан простой базовый обьект (object).

Пример выполнения:
mc1 = MyClass("A")   --> MyClass obj
mc2 = MyClass("A")        --> MyClass obj
not_mc1 = MyClass("C")     --> object
not_mc2 = MyClass("B","C")     --> object"""


class MyClass:
    def __new__(cls, *args, **kwargs):
        if "B" and "C" in args:
            return object()
        elif len(args) == 1:
            if "C" in args:
                return object()
            elif "A" or "B" in args:
                return super(MyClass, cls).__new__(cls)
            else:
                raise AssertionError

    def __init__(self, *args):
        self.elements = args

    def __str__(self):
        return f"{self.__class__.__name__}"
