"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
def merge_sort(data):
    if len(data) > 1:
        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        left_size = len(left)
        right_size = len(right)

        while i < left_size and j < right_size:
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < left_size:
            data[k] = left[i]
            i += 1
            k += 1

        while j < right_size:
            data[k] = right[j]
            j += 1
            k += 1
    return data



import random
SIZE = 10
array = [random.uniform(0, 49.99) for _ in range(SIZE)]
res_array = []
print(array)
print(merge_sort(array))
