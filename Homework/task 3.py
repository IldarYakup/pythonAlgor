"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random
MIN_NUM = 0
MAX_NUM = 50
m = random.randint(1, 10)
array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(2 * m + 1)]
res_array = array.copy()
before_median = []
post_median = []

#Использовать попарное исключение максимального и минимального значения, в конечном итоге остается одно число, которое и является медианой.
while m != 0:
    max_num = MIN_NUM
    min_num = MAX_NUM
    for i in range(0, len(res_array)):
        if res_array[i] > max_num:
            max_num = res_array[i]
    post_median.append(max_num)
    res_array.remove(max_num)
    for i in range(0, len(res_array)):
        if res_array[i] < min_num:
            min_num = res_array[i]
    before_median.append(min_num)
    res_array.remove(min_num)
    m -= 1

print(f'Медианой в массиве {array} является {res_array[0]}')
print(f"Проверка медианы:\nМассив чисел перед медианой в количестве {len(before_median)} значений - {before_median} \nМассив чисел после медианы в количестве {len(post_median)} значений - {post_median} ")
