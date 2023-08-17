# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.


def read_n_write_files(name_file_names: str, name_file_numbers: str, result_file: str) -> None:

    with open(name_file_names, 'r', encoding='utf-8') as file_names, open(name_file_numbers, 'r', encoding='utf-8') as file_numbers:
        names = file_names.read().split('\n')
        numbers = file_numbers.read().split('\n')

    if len(numbers) > len(names):
        names += names[:len(numbers) - len(names)]
    else:
        numbers += numbers[:len(names) - len(numbers)]

    with open(result_file, 'w', encoding='utf-8') as result_file:
        for name, number in zip(names, numbers):
            if not name or not number:
                break
            number_result_int, number_result_float = map(float, number.split(' | '))
            multiply: float = number_result_int*number_result_float

            if multiply < 0:
                result_file.write(f'{name.lower()} {abs(multiply)} \n')
            else:
                result_file.write(f'{name.upper()} {int(multiply)} \n')


if __name__=='__main__':
    read_n_write_files(name_file_names='name_file_task.txt', name_file_numbers='file_numbers.txt', result_file='result_file.txt')
