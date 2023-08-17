"""Создайте функцию для сортировки файлов по директориям:
видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
from os import chdir, mkdir,listdir, getcwd
from pathlib import Path


def sort_files_by_extension_to_directory(directory: str | Path = 'test_dir'):
    chdir(directory)
    print(listdir())
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        extention = file.name.split('.')[1]
        if extention.upper() not in listdir():
            mkdir(extention.upper())
        file.replace(f'{extention.upper()}\\{file.name}')


if __name__=='__main__':
    sort_files_by_extension_to_directory()