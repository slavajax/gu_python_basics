database = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

analytics = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}


def show_menu():
    """ Show program menu """
    print('Menu:')
    print('Press [M] to show menu program.')
    print('Press [Q] to exit the program.')
    print('Press [1] to show all records.')
    print('Press [2] to show analytics.')
    print('Press [3] to add an entry to the database.')
    print('')


def show_row_table():
    """ Render first row table """
    row = list(database[0][1].keys())
    row.insert(0, '№')
    print(u'Список товаров \u2193')
    print(u'\u035F' * 38)
    print(' | '.join(row))
    print(u'\u035E' * 38)


def show_database():
    """ Show all records in database """
    show_row_table()
    for i, record in enumerate(database):
        print(f'{i + 1} '
              f'| {database[i][1]["название"]} '
              f'| {database[i][1]["цена"]} '
              f'| {database[i][1]["количество"]} '
              f'| {database[i][1]["eд"]}')


def get_analytics():
    """ Getting analytical data from the database """
    for i, record in enumerate(database):
        analytics['название'].append(database[i][1]['название'])
        analytics['цена'].append(database[i][1]['цена'])
        analytics['количество'].append(database[i][1]['количество'])
        if 'шт.' not in analytics['ед']:
            analytics['ед'].append('шт.')


def print_analytics():
    """ Print the analysis """
    print(u"Аналитика по БД \u2605")
    print('название: ', end='')
    print(u"\u25B6", end=' ')
    print(', '.join(analytics['название']))
    print('цена: ', end='')
    print(u"\u25B6", end=' ')
    print(', '.join(str(price) for price in analytics['цена']))
    print('количество: ', end='')
    print(u"\u25B6", end=' ')
    print(', '.join(str(price) for price in analytics['количество']))
    print('ед: ', end='')
    print(u"\u25B6", end=' ')
    print(', '.join(analytics['ед']))


def add_rec_to_database():
    """ Adding a record to the database """
    print(u'Добавление нового товара \u2193 \n')
    name = input('Введите название товара: ')

    while True:
        try:
            price = int(input('Введите стоимость товара: '))
            break
        except ValueError:
            print('Пожалуйста, введите число.')

    while True:
        try:
            quantity = int(input('Введите количество товара: '))
            break
        except ValueError:
            print('Пожалуйста, введите число.')

    data = {'название': name, 'цена': price, 'количество': quantity, 'eд': 'шт.'}
    database.append((database[-1][0] + 1, data))


show_menu()

while True:
    command = input('Enter the command ([M] - menu): ')

    if command == 'M':
        show_menu()
    elif command == '1':
        show_database()
        input()
    elif command == '2':
        get_analytics()
        print_analytics()
        input()
    elif command == '3':
        add_rec_to_database()
    elif command == 'Q':
        break

print('The program is finished.')
