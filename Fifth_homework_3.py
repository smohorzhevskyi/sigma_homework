"""Напишите декоратор, который принимает 2 аргумента – html tag и число N.
В результате декорирования функции, которая принимает аргументом строку вы должны получить список строк длиной N
в формате <html tag> строка с заглавной буквы + порядковый номер элемента в списке, начиная с 1</html tag >.
Если строка, передаваемая в качестве аргумента функции, содержит спецсимволы @, #, %, &, $, ^, *, _
нужно каждый из них заменить на пробел, а символы <, >, / удалить из строки.

Пример:
@html_decorator("li", 3)
def html_element(text):
       …

print(html_element('>list_item<'))

Результат:

['<li>List item 1</li>', '<li>List item 2</li>', '<li>List item 3</li>']

"""


def html_decorator(html_tag, N):
    def inner_decorator(function):
        def wrapper(string):
            list_result = []
            chars = '@#%&$^*_'
            for char in chars:
                string = string.replace(char, ' ').strip()
            chars = '<>/'
            for char in chars:
                string = string.replace(char, '').strip()
            for i in range(1, N+1):
                element = f"<{html_tag}>{string.capitalize()} {i}</{html_tag}>"
                list_result.append(element)
            return list_result
        return wrapper
    return inner_decorator


@html_decorator("li", 3)
def html_element(string):
    pass


print(html_element('>list_item<'))
