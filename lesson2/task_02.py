# Первый вариант решений
user_values = input('Enter the number without space: ')
user_numbers = list(user_values.replace(' ', ''))

for i in range(1, len(user_numbers), 2):
    user_numbers[i - 1], user_numbers[i] = user_numbers[i], user_numbers[i - 1]

print(user_numbers)

# Второй вариант решения
user_values = input('Enter the number with space: ').split()
user_values_list_len = len(user_values)

idx = user_values_list_len if user_values_list_len % 2 == 0 else user_values_list_len - 1
user_values[:idx:2], user_values[1:idx:2] = user_values[1:idx:2], user_values[:idx:2]

print(f'Result your list: {user_values}')
