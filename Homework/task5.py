"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
second_array = []
for i in range(0, len(array)):
    if array[i] < 0:
        second_array.append(array[i])
max_num = second_array[0]
for i in range(0, len(second_array)):
    if second_array[i] > max_num:
        max_num = second_array[i]
print(f'Максимальное отрицательное число в списке {max_num} и находится  на позиции "{array.index(max_num)+1}" и имеет индекс "{array.index(max_num)}"')