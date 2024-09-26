"""Напишите   класс   итератор   Circle,   который   принимает   два аргумента   -   последовательность   и   число.
При   прохождение циклом   по   объекту   данного   класса   на   каждой   итерации   выдолжны получать
следующий элемент последовательности и если число (второй аргумент)  больше, чем количество элементов, то
последовательность повторяется с начала. Попробуйте для этой задачи создать отдельный класс для итератора -
CircleIterator.
Аргументы:
seasons = [‘Winter’, ‘Spring’, ‘Summer’, ‘Autumn’
max_times = 7

Цикл должен сгенерировать следующее:
Winter
Spring
Summer
Autumn
Winter
Spring
Summer
"""


class Circle:
    class CircleIterator:
        def __init__(self, outer_words, outer_number):
            self.words_list = outer_words
            self.given_number = outer_number
            self.length = len(self.words_list)
            self.x = 0
            self.occ = 0

        def __iter__(self):
            return self

        def __next__(self):
            self.occ += 1

            if self.occ <= self.given_number:
                if self.x < self.length:
                    self.x += 1
                    return self.words_list[self.x-1]
                if self.x == self.length:
                    self.x = 0
                    self.x += 1
                    return self.words_list[self.x-1]
            else:
                raise StopIteration

    def __init__(self, words_list, given_number):
        self.words_list = words_list
        self.given_number = given_number

    def __iter__(self):
        return self.CircleIterator(self.words_list, self.given_number)


seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
max_times = 7

my_iter = Circle(seasons, max_times)
print(iter(my_iter))

for i in my_iter:
    print(i)
