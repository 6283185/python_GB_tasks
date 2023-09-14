# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов,
# которые также являются свойствами экземпляра.

class Archive:
    """Архив хранения свойств."""
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """Создание нового архива."""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        """Инициализация архива."""
        self.number = number
        self.value = value


if __name__ == '__main__':
    a_1 = Archive(1, "Один")
    a_2 = Archive(2, "Два")
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3, "Три")
    print(f'{a_3.numbers} {a_3.values}')