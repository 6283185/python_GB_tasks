try:
    a, b, c = int(i) for i in input('Введите стороны треугольника через пробел: ').split()
    if a + b <= c or a + c <= b or b + c <= a:
      raise TriangleException("Стороны треугольника не могут быть отрицательными")
    # Остальной код
except TriangleException as e:
    print("Ошибка: {}".format(e))
