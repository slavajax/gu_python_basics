total_month = 12
db_seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
db_months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
             'декабрь']

while True:
    user_month = input('Введите номер месяца от 1 до 12: ')
    if user_month.isdigit() and 0 < int(user_month) <= total_month:
        user_month = int(user_month)
        for season, month in db_seasons.items():
            if user_month in month:
                print(f'Месяц {db_months[user_month - 1].upper()} '
                      f'- прекрасное время года под названием {season.upper()}!')
                break
    else:
        print('Введены некорректные данные')
        break
