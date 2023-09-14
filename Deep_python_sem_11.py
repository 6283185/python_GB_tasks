# Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора
# строки и время создания (time.time)

import time


class MyString(str):
    """Расширенный класс строки."""

    def __new__(cls, value: str, name: str):
        """Инициализация класса.

        :value: Значение строки.
        :name: Имя автора строки.
        """
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance


if __name__ == '__main__':
    mystr = MyString('САМА строка', 'доп. параметр')
    print(mystr.name)
    print(mystr.created_at)
    print(mystr)
    print(mystr.upper())