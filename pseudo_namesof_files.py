# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные. Полученные имена сохраните в файл.
from random import randint


def file_naming() -> str:
    name = ''
    for i in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def added_in_file_name(file_name: str, count_line: int):
    file_name += '.txt'

    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(count_line):
            file.write(f'{file_naming()} \n')


if __name__=='__main__':
    added_in_file_name('name_file_task', 5)