# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число в десятичной системе: '))


def ten_to_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result


print(f'Число преобразованное собственной функцией в шестнадцатеричное = {ten_to_hex(num)}, встроенной функцией hex = {hex(num)}')
