# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть шестизначный идентификационный номер
# и уровень доступа (остаток от суммы цифр id делённой на семь).
import random

def sum_digits(a: int):
    a = str(a)
    sum_a = 0
    for i in a:
        sum_a += int(i)
    return sum_a % 7


class Person:
    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

class Employee(Person):
    def __init__(self, surname, name, patronymic, age):
        super().__init__(surname, name, patronymic, age)
        self.id = random.randint(100000, 999999)
        self.level = sum_digits(self.id)

if __name__ == '__main__':
    p1 = Employee('Chernyshov', 'Dmitriy', 'Igorevich', 38)
    print(p1, p1.get_age(), p1.id, p1.level)
