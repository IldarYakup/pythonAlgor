"""
В одномерном массиве найти сумму элементов,
 находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.
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
sum_element = 0
if array.index(min_num) < array.index(max_num):
    for i in range((array.index(min_num)+1), (array.index(max_num))):
        sum_element += array[i]
elif array.index(min_num) > array.index(max_num):
    for i in range((array.index(max_num) + 1), (array.index(min_num))):
        sum_element += array[i]
print(f'Минимальный элемент в списке {min_num}, максимальный элемент в списке {max_num}\nсумма элементов между минимальным и максимальным элементом {sum_element}')

