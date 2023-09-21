'''
расчет площади, периметра прямоугольника,
селадывание и вычитание двух прямоугольников

'''

from exeptions.rectangle_exeptions import ValError

class Rectangle:

    def __init__(self, side_a: float, side_b: float):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)


    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __str__(self):
        return f"В результате - прямоугольник со сторонами: {self._side_a}   {self._side_b}, периметром: {self.get_perimeter()}, площадью: {self.get_area()}"





if __name__ == '__main__':
    try:
        a_1, a_2 = (float(i) for i in input('Введите стороны прямоугольника через пробел: ').split())


    except ValueError as e:
        print(f"\nНеправильный формат ввода данных: {e}.\nПо умолчанию стороны прямоугольника равны.\n")
        if a_1 <= 0 or a_2 <= 0:
            raise ValError(a_1, a_2)

    rectangle_1 = Rectangle(a_1, a_2)
    print(f'{rectangle_1.get_perimeter() = },  {rectangle_1.get_area() = }')





