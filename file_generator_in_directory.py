"""Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию - отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файла не должны удаляться/изменяться в случае совпадения имён."""
from os import getcwd, listdir, mkdir
from random import randint, choice

def file_naming() -> str:
    name: str = ''
    for i in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def mk_file(extension: str, directory: str = None, min_len: int = 6,
            max_len: int = 30, min_size: int = 256,
            max_size: int = 4096, count_files: int = 42):
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '\\' + directory +'\\'

    print(directory)
    for i in range(count_files):
        with open(directory + file_naming() + extension, 'w', encoding='utf-8') as file_output:
            list_of_bytes = bytes([randint(0, 255) for x in range(min_size, max_size)])
            file_output.write(str(list_of_bytes))


if __name__ == '__main__':
    EXT = ('.txt', '.doc', '.pdf', '.jpg')
    mk_file(extension=choice(EXT), directory='test_dir', count_files=5)
