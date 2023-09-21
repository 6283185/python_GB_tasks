class TriangleException(ValueError):
    def __str__(self) -> str:
        return f"Нельзя создать треугольник данными сторонами {self._size}"
