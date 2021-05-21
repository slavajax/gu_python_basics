# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_func(n1, n2, n3):
    """ Нахождение минимального числа, затем удаление """
    numbers = [n1, n2, n3]
    numbers.remove(min(numbers))
    return sum(numbers)


def my_func_v2(n1, n2, n3):
    """ Сортировка, затем срез """
    numbers = [n1, n2, n3]
    return sum(sorted(numbers)[1:])


def my_func_v3(n1, n2, n3):
    """ Получить сумму всех элементов, затем найти и вычесть минимальное """
    numbers = [n1, n2, n3]
    return sum(numbers) - min(numbers)


print(my_func_v3(3, 1, 2))
