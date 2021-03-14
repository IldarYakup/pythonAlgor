"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
#
import random
import timeit
import cProfile


size = 1
while size != 10000:
    size *= 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
second_array = []

# вариант 1

def negative_number_var1(size):
    for i in range(len(array)):
        if array[i] < 0:
            second_array.append(array[i])
    max_num = second_array[0]
    for i in range(0, len(second_array)):
        if second_array[i] >= max_num:
            max_num = second_array[i]
    return f'Максимальное отрицательное число в списке {max_num} и находится  на позиции "{array.index(max_num)+1}" и имеет индекс "{array.index(max_num)}"'


# вариант 2

def negative_number_var2(size):
    i = 0
    index = -1
    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        return f'Максимальное отрицательное число {array[index]} '
        f'находится в ячейке {index}'

# вариант 3

def negative_number_var3(size):
    num = float('-inf')
    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i

    if num != float('-inf'):
        return f'Максимальное отрицательное число {num} '
        f'находится в ячейке {index}'

print(timeit.timeit('negative_number_var1(10)', number=100, globals=globals()))            #3.3536626999999997
print(timeit.timeit('negative_number_var1(100)', number=100, globals=globals()))           #9.5828594
print(timeit.timeit('negative_number_var1(1000)', number=100, globals=globals()))          #15.8068749
print(timeit.timeit('negative_number_var1(10000)', number=100, globals=globals()))         #22.3910529

cProfile.run('negative_number_var1(10000)')
"""
4980 function calls in 0.266 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.266    0.266 <string>:1(<module>)
        1    0.265    0.265    0.266    0.266 task1.py:24(negative_number_var1)
        1    0.000    0.000    0.266    0.266 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     4972    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        """

print(timeit.timeit('negative_number_var2(10)', number=100, globals=globals()))          #0.4859530000000021
print(timeit.timeit('negative_number_var2(100)', number=100, globals=globals()))         #0.4846116000000009
print(timeit.timeit('negative_number_var2(1000)', number=100, globals=globals()))        #0.48770700000000033
print(timeit.timeit('negative_number_var2(10000)', number=100, globals=globals()))       #0.49274520000000166

cProfile.run('negative_number_var2(10000)')
"""
10005 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.006    0.006    0.008    0.008 task1.py:37(negative_number_var2)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
    10001    0.002    0.000    0.002    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print(timeit.timeit('negative_number_var3(10)', number=100, globals=globals()))         #0.1330067000000028
print(timeit.timeit('negative_number_var3(100)', number=100, globals=globals()))        #0.13350899999999655
print(timeit.timeit('negative_number_var3(1000)', number=100, globals=globals()))       #0.13369949999999875
print(timeit.timeit('negative_number_var3(10000)', number=100, globals=globals()))      #0.13113059999999876

cProfile.run('negative_number_var3(10000)')
"""
4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task1.py:53(negative_number_var3)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""



"""
Наиболее быстрым и лучшим вариантом оказался вариант №3.
В варианте №1 главным "тормозом" оказался метод append, добавляющий в новый список только отрицательные числа.
В варианте №2 главным "тормозом" оказался Len, который каждый цикл определяет длину массива.
Вариант №3 оказался наиболее быстрым, из-за наименьшего количества переменых и действий.
"""