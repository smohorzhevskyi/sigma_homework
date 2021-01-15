"""
Перепишите   задачу   No1   в   виде   функции   генератора   и генераторного выражения.
"""

test_sentence = 'Hello my name is pony'


# Генератор
def sentence(string):
    words_list = string.split()
    for one_word in words_list:
        yield one_word


generator = sentence(test_sentence)
for word in generator:
    print(word)

# Генераторное выражение

generator_sentence = (word for word in test_sentence.split())
for word in generator_sentence:
    print(word)

