class TriangleError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Нельзя создать треугольник с данными сторонами!"
