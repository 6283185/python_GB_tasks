# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.
from random import randint, uniform


def added_in_file_numbers(file_name: str, count_line: int):
    file_name += '.txt'

    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(count_line):
            file.write(f'{randint(-1000, 1000)} | {round(uniform(-1000, 1000), 2)} \n')


if __name__=='__main__':
    added_in_file_numbers('file_numbers', 5)