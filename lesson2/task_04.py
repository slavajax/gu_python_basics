user_words = input('Введите строку, состоящую из несколько слов: ').split()

for num, word in enumerate(user_words, 1):
    print(num, word[:10])
