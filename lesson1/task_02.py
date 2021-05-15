'''
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

user_input = input('Введите время в секундах: ')

if not user_input.isdigit():
    print('Пожалуйста, вводите только цифры.')
    exit()

seconds_in_hour = 3600  # секунд в одном часе
minutes_in_hour = 60  # минут в одном часе

# Перевести принятую от пользователя строку в число
user_seconds = int(user_input)

hours = user_seconds // seconds_in_hour
minutes = (user_seconds % seconds_in_hour) // minutes_in_hour
seconds = (user_seconds % seconds_in_hour) % minutes_in_hour

print(f'Введенное время (отформатированное) -> {hours:>02}:{minutes:>02}:{seconds:>02}')
