# Создайте функцию генератор чисел Фибоначчи

quantity_fibonacci_numbers = int(input('Введите количество чисел последовательности Фибоначчи: '))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


res = fib(quantity_fibonacci_numbers)
print(list(res))