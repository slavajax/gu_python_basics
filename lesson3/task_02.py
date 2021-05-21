# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

def user_info(name, surname, birthday, city, email, phone):
    return f'Name - {name}, Surname - {surname}, Birthday - {birthday}, ' \
           f'City - {city}, Email - {email}, Phone - {phone}'


print(user_info(name='Name', surname='Surname', birthday='01.01.1970',
                city='City', email='email@email.email', phone='Phone'))
