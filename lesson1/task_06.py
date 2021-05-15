start_value = int(input('Сколько сейчас км пробегает спортсмен? '))
end_value = int(input('Сколько км нужно пробегать спортсмену? '))

# За сколько дней тренировок спортсмен добьется результата
training_days = 1

while start_value < end_value:
    start_value += start_value * 0.1
    training_days += 1

print(f'на {training_days}-й день спортсмен достиг результата — не менее 3 км.')
