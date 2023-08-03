# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


import random

a = {"water": 40, "meat": 40, "bread": 10, "tent": 50, "coal": 30, "beer": 20, "whiskey": 30}

maximum_load = 100
counter = 0
List_atribute = []
while counter < maximum_load:
    key, value = random.choice(list(a.items()))
    if key in List_atribute:
        continue
    if counter + value > maximum_load:
        break
    counter += value
    List_atribute += (str(key), str(value))

print(List_atribute, "=", counter)