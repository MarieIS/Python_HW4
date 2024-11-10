s = str(input('Введите вашу строку: '))
array = list(s)

myset = set(array)
num = len(array) - 2 * len(myset)

if (num == 1) or (num == 0):
    print('Из введенной строки можно создать палиндром')
else:
    print('Из введенной строки нельзя создать палиндром')