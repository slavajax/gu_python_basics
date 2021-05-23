```python
try:
    user_input = int(input('Введите время в секундах: '))
except ValueError:
    print('Вы ввели неверное значении или ввели пустую строку.')

hours = user_input // 3600
minutes = user_input % 3600 // 60
seconds = user_input % 3600 % 60
print(f'{hours:>02}:{minutes:>02}:{seconds:>02}')

```

    Введите время в секундах: 3800
    01:03:20
    
