# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

import math


class Rectangle:
    def __init__(self, lenght: float, width: float = None) -> None:
        self.lenght = lenght
        if width:
            self.width = width
        else:
            self.width = lenght

    def perimetr(self):
        return (self.lenght + self.width) * 2


    def calc_area(self):
        return self.width + self.lenght


if __name__ == '__main__':
    r1 = Rectangle(2, 3)
    print(f'{r1.perimetr() = }\n{r1.calc_area() = }')

    r2 = Rectangle(3)
    print(f'{r2.perimetr() = }\n{r2.calc_area() = }')