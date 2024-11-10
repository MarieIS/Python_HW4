# функция для создания словаря частот символов

def histogram(string):
    sym_dict = dict() # инициализируем пустой словарь для частот
    for sym in string:
        # если символ уже есть в словаре, увеличиваем его частоту
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            # если символа нет в словаре, добавляем его с частотой 1
            sym_dict[sym] = 1
    return sym_dict

# функция для инвертирования словаря частот
def invert_dict(d):
    inv = dict() # инициализируем пустой словарь для инвертированных данных
    for key in d:
        val = d[key]
        # если частота еще не встречалась, создаем новый список
        if val not in inv:
            inv[val] = [key]
        else:
            # если частота уже есть в словаре, добавляем символ в существующий список
            inv[val].append(key)
    return inv

# запрашиваем текст у пользователя
text = input('Введите текст: ')
# создаем словарь частот
hist = histogram(text)

# выводим оригинальный словарь частот
print('Оригинальный словарь частот: ')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

# создаем инвертированный словарь частот
inv_hist = invert_dict(hist)

# выводим инвертированный словарь частот
print('Инвертированный словарь частот: ')
for i_sym in sorted(inv_hist.keys()):
    print(i_sym, ':', inv_hist[i_sym])