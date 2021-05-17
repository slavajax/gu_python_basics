rating = list(map(int, input('Введите оценки рейтинга через пробел: ').split()))
rating_updated = rating.copy()

while True:
    try:
        user_rating = int(input('Введите новое значение рейтинга: '))
        if user_rating > 0:
            rate_index = 0
            for rate in rating_updated:
                if user_rating <= rate:
                    rate_index += 1
            rating_updated.insert(rate_index, user_rating)
            print(f'Новое значение успешно добавлено: {rating_updated}')
        else:
            print('Построение рейтинга завершено.')
            break
    except ValueError:
        print('Так каши не сваришь! Нужно ввести корректное значение.')

print(f'Рейтинг до изменения: {rating}')
print(f'Рейтинг после изменений {rating_updated}')
