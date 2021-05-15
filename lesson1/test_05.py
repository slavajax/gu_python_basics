'''
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток
— издержки больше выручки). Выведите соответствующее сообщение. Если фирма
отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к
выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
расчете на одного сотрудника.
'''

revenue = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))

profit = revenue - costs

if profit > 0:
    print(f'Ваша компания работает с прибылью {profit} р.')
    print(f'Рентабельность вашей организации составляет {profit / revenue:.2f} %')

    employees_count = int(input('Сколько сотрудников работает в вашей организации? '))
    print(f'Итого: каждый сотрудник может получить по {profit / employees_count:.2f} р.')

elif profit < 0:
    print(f'Ваша организация сработала в убыток - {profit}')
else:
    print(f'Все еще не так страшно! Ваша организация сработала в 0.')
