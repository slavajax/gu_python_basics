# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def div(f, s, integer=True):
    """ Выполняет деление a на b """
    try:
        if integer:
            return int(f / s)
        return float(f / s)
    except ZeroDivisionError:
        return 'Деление на 0 запрещено.'


a = None  # Объявление переменной
a_valid = False  # Если значение валидно, то True

b = None  # Объявление переменной
b_valid = False  # Если значение валидно, то True

while True:
    if not a_valid:
        a = input('Введите первое число: ')
        if not a.isdigit():
            print('Пожалуйста, используйте только числа.')
            continue
        a = int(a)
        a_valid = True

    if not b_valid:
        b = input('Введите второе число: ')
        if not b.isdigit():
            print('Пожалуйста, используйте только числа.')
            continue
        b = int(b)
        b_valid = True

    print(div(a, b, integer=False))
    break
