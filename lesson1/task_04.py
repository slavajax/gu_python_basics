'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
digit = int(input('Введите целое положительное число: '))

if digit < 10:
    print(f'Наибольшая цифра с числе {digit} равна {digit}')
    exit()

digit_max = digit % 10  # предположительно последняя цифра является максимумом
digit_queue = digit  # очередь из цифр числа

while digit_queue > 0:
    if digit_max == 9:
        break

    digit_max = digit_queue % 10
    digit_queue //= 10

print(f'Наибольшая цифра с числе {digit} равна {digit_max}')
