# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint


def game(start: int, end: int, tries: int) -> bool:
    num = randint(start, end)
    for _ in range(tries):
        enter = int(input("Отгадайте заданное число: "))
        if num > enter:
            print("больше")
        elif num < enter:
            print("меньше")
        else:
            return True
    return False

if __name__=='__main__':
    print(game(3, 10, 3))

