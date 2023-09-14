"""
Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры,
а не длинну и ширину. При вычитании не допускайте отрицательных значений.
"""
__all__ = ['Rectangle']


class Rectangle:
    """Класс Прямоугольник."""

    def __init__(self, a: int, b: int = None):
        """Инициализация нового экземпляра."""
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        """Расчет периметра прямоугольника."""
        return 2 * (self.a + self.b)

    def area(self):
        """Расчет площади прямоугольника."""
        return self.a * self.b

    def __add__(self, other):
        """Сложение двух прямоугольников."""
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        """Вычитание прямоугольников."""
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)


if __name__ == '__main__':
    rect_1 = Rectangle(2, 5)
    rect_2 = Rectangle(5, 10)
    res_sum = rect_1 + rect_2
    print(res_sum.a, res_sum.b)
    res_sub = rect_1 - rect_2
    print(res_sub.a, res_sub.b)