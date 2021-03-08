"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max_num = array[0]
for i in range(0, len(array)):
    if array[i] > max_num:
        max_num = array[i]
min_num = array[0]
for i in range(0, len(array)):
    if array[i] < min_num:
        min_num = array[i]
print(f'Максимальное число в списке - "{max_num}" и находится на "{array.index(max_num)+1}" позиции списка')
print(f'Минимальное число в списке - "{min_num}" и находится на "{array.index(min_num)+1}" позиции списка')

first_el = array[array.index(max_num)]
second_el = array[array.index(min_num)]
first_index = array.index(max_num)
second_index = array.index(min_num)
array.insert(first_index, second_el)
array.pop(first_index+1)
array.insert(second_index, first_el)
array.pop(second_index+1)
print(f'Производим замену местами максимального и минимального значения\n{array}')

