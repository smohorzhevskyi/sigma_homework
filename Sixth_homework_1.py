"""Напишите класс итератор Sentence, который  принимает строку,состоящую из нескольких слов,
разделенных пробелом в качестве аргумента. При прохождение циклом по объекту данного класса на каждой итерации
вы должны получать следующее слово из этой строки."""


class Sentence:

    def __init__(self, string):
        self.list = string.split()
        self.index_value = 0
        self.index_end = len(self.list) - 1

    def __iter__(self):
        return iter(self.list)

    def __next__(self):
        if self.index_value > self.index_end:
            raise StopIteration
        current = self.index_value
        self.index_value += 1
        return self.list[current]


my_iter = Sentence("Hello my name is pony")
print(iter(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
