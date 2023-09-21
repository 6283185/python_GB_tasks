from exeptions.is_triangle_exist_exception import TriangleError


def check_triangle_existence(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise TriangleError("Треугольника с такими сторонами не существует")

def main():
    try:
        a, b, c = (int(i) for i in input('Введите стороны треугольника через пробел: ').split())
        check_triangle_existence(a, b, c)
        if a == b == c:
            print("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    except ValueError:
        print("Ошибка: введите целые числа для сторон треугольника")
    except TriangleError as error:
        print(error)

if __name__ == "__main__":
    main()
