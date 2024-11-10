N = int(input('Введите количество пар слов: '))
print('Давайте составим ваш персональный словарь')
d = dict()

for i in range(N):
    key = str(input(f'Введите слово № {i+1}: ').lower())
    d[key] = str(input('Введите его синоним: ').lower())

print('Словарь создан')

print('Введите ваше слово, а мы найдем его синоним')

value = str(input('Ваше слово: ').lower())

if value in d:
    print(d[value])
else: print('Такого слова нет')