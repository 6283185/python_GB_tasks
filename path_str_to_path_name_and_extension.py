# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

path_abs = "C:/Users/Home/Шерсть.fb2"


def path_to_name_n_path_n_extention(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

res = path_to_name_n_path_n_extention(path_abs)
print(f'Абсолютный путь к файлу: {path_abs}')
print(f'Путь к файлу: {res[0]} \nИмя файла: {res[1]} \nРасширение: {res[2]}')
