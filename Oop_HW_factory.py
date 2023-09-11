# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.




from Oop_5_animals import Animal, Dog, Kotopes, Fish


class AnimalFactory:
    def __init__(self, animal_class: str, **kwargs):
        self.animal_class = animal_class

        for key, i in kwargs.items():
            if key == 'name':
                self.name = i
            if key == 'age':
                self.age = i
            if key == 'color':
                self.color = i
            if key == 'is_domestic':
                self.is_domestic = i
            if key == 'number_heads':
                self.number_heads = i
            if key == 'aqua':
                self.aqua = i
            if key == 'size':
                self.size = i

    def get_info_animal(self):
        if self.animal_class == 'Kotopes':
            return Kotopes(self.name, self.age, self.number_heads)
        elif self.animal_class == 'Dog':
            return Dog(self.name, self.age, self.color, self.is_domestic)
        elif self.animal_class == 'Fish':
            return Fish(self.name, self.age, self.aqua, self.size)
        else:
            return f'Неизвестное животное!'


if __name__ == '__main__':
    animal1 = AnimalFactory(animal_class='Kotopes', age=3, name='Котопёс младший', number_heads=2).get_info_animal()
    animal2 = AnimalFactory(animal_class ='Dog', name='Тузик', age=8, color='Белый', is_domestic=False).get_info_animal()
    print(animal1)
    print(animal2)