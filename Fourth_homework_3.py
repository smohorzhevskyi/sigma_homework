"""
Создайте  класс   Employee,   который   принимает   имя,   фамилию   и зарплату   в  качестве  аргументов
при   конструировании.   При   этом Employee   является   дочерним   классом   Human. Класс   Human
принимает first_name и last_name в качестве аргументов и реализует метод full_name.
Класс Employee должен поддерживать:
 атрибут first_name, возвращающий имя
 атрибут last_name, возвращающий фамилию
 атрибут salary, возвращающий зарплату
 метод full_name, который возвращает полное имя сотрудника.
 метод from_string, которая принимает имя, фамилию и зарплату в формате
'first_name-last_name-salary', парсит строку и возвращает экземпляр Employee
Также   обратите   внимание,   что   в   методах/атрибутах,   которые возвращают   имя,   фамилию
или   полное   имя   необходимо,   чтобы   эти данные возвращались в виде строки, которая начинается с заглавной буквы
Примеры:
emp1 = Employee('JOAN', 'Smith', 85000)
emp2 = Employee.from_string('John-doe-73000')
emp1.first_name ➞ 'Joan'
emp1.full_name ➞ 'Joan Smith'
emp1.salary ➞ 85000
emp2.first_name ➞ 'John'
emp2.full_name ➞ 'John Doe'
emp2.salary ➞73000
"""


class Human:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    @property
    def full_name(self):
        return f"'{self.first_name} {self.last_name}'"


class Employee(Human):

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    @staticmethod
    def from_string(string):
        my_list = string.split("-")
        return Employee(*my_list)


emp1 = Employee('JOAN', 'Smith', 85000)
emp2 = Employee.from_string('John-doe-73000')
print(emp1.first_name)
print(emp1.full_name)
print(emp1.salary)
print(emp2.first_name)
print(emp2.full_name)
print(emp2.salary)
