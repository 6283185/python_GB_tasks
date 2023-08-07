# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_matrix(matrix: list[list[int | float]]):
    for row in matrix:
        print(f"{row}", end="\t")
        print()


def transpose(matrix: list[list[int | float]]):

    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]


print("Исходная матрица")
print_matrix(matrix)
transpositoned_matrix = transpose(matrix)
print("Транспонированная матрица")
print_matrix(transpositoned_matrix)