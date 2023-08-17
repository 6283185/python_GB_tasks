"""Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона."""

"""Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи."""

from random import randint, choice

EXT = ('.txt', '.doc', '.pdf', '.jpg')


def file_naming() -> str:
    name: str = ''
    for i in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def mk_file(extension: str, min_len: int = 6,
            max_len: int = 30, min_size: int = 256,
            max_size: int = 4096, count_files: int = 42):
    for i in range(count_files):
        with open(file_naming() +extension, 'w', encoding='utf-8') as file_output:
            list_of_bytes = bytes([randint(0, 255) for x in range(min_size, max_size)])
            file_output.write(str(list_of_bytes))


def create_different_extention_files():
    extention = choice(EXT)
    mk_file(extension=extention)

if __name__=='__main__':
    create_different_extention_files()