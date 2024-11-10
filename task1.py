array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# from array to set:
set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)

# intersection of sets:
set_uniq1 = set_1 & set_2 & set_3
print('Эти элементы есть в каждом из множеств: ', set_uniq1)

# elements from the first set:
set_uniq2 = set_1 - set_2 - set_3
print('Эти элементы есть только в первом множестве: ', set_uniq2)