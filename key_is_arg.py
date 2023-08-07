# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def key_is_arg(**kwargs):
    reverse_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        reverse_dict[value] = key
    return reverse_dict


print(key_is_arg(students=["Ivan", "Masha"], frends={1: "Sergey", 2: "Jack", 3: "Max"}, fruits=["apple", "orange", "banana"]))