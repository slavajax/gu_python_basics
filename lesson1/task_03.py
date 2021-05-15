'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
user_input = input('Введите число от 0 до 9: ')

if not user_input.isdigit():
    print('Вы ввели неверное число.')
    exit()

result = 0
for x in range(1, 4):
    result += int(user_input * x)

print(f'Результат вычислений: {user_input} + {user_input * 2} + {user_input * 3} = {result}')
