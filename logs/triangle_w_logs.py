import logging

logging.basicConfig(filename='error.log', filemode='a', encoding = "UTF-8",style='{', level=logging.DEBUG)


def is_triangle_exist(a: float, b: float, c: float):
    if a + b <= c or a + c <= b or b + c <= a:
        logging.error("Треугольника с такими сторонами не существует: %d, %d, %d", a, b, c)
        print("Треугольника с такими сторонами не существует")
    else:
        if a == b == c:
            print("Треугольник равносторонний")
            logging.info("Треугольник равносторонний: %d, %d, %d", a, b, c)

        # elif (a not int()) or (b not int()) or (c not int()):


        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
            logging.info("Треугольник равнобедренный: %d, %d, %d", a, b, c)

        else:
            print("Треугольник разносторонний")
            logging.info("Треугольник разносторонний: %d, %d, %d", a, b, c)


if __name__ == "__main__":
    a, b, c = (float(i) for i in input('Введите стороны треугольника через пробел: ').split())
    is_triangle_exist(a, b, c)
