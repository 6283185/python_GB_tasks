# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
#
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv
import os
from pathlib import Path


def group_rename(count_nums: int, extention_old: str, extention_new: str, diapazon: list[int], wanted_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extention_old):
            count += 1
            Path(file).rename(f"{file.split('.')[0][diapazon[0]:diapazon[1]]}{wanted_name}{count:0>{count_nums}}.{extention_new}")



if __name__=='__main__':
    group_rename(wanted_name = "video", count_nums=3, extention_old=".txt", extention_new=".csv", diapazon=[3, 6])