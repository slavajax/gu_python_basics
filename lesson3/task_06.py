# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
# Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

def int_func(word):
    for ch in word:
        char_ord = ord(ch)
        if char_ord < 97 or char_ord > 127:
            print('The word must consist only of Latin letters.')
            return ''
        return word.title()


result = ''
for word in input('Enter words with a space (lower latin): ').split():
    result += f'{int_func(word)} '
print(' '.join(result.split()))
