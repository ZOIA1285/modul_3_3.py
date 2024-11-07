# Создаём функцию, которая принимает 3 параметра со значением по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    # Функция должна выводить эти параметры
    print(a, b, c)
# Вызыаем функцию print_params с разным количеством аргументов,
# включая вызов без аргументов
print_params(a = 1, c = True )
print_params()
# Проверяем, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров:
# Создаём список values_list с тремя элементами разных типов
values_list = ['КНИГА', 3.14, 39 ]
# Создаём словарь values_dict с тремя ключами, соответствующими параметрам
# функции print_params, и значениями разных типов.
values_dict = {'a': 1, 'b': 'строка', 'c': True}
# Передаём values_list и values_dict в функцию print_params, используя
# распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
# Распаковка + отдельные параметры
print(values_list)
print_params(values_dict)
# Создаём список values_list_2 с двумя элементами разных типов
values_list_2 = [False, "ГАЗЕТА"]
# Проверяем, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)




