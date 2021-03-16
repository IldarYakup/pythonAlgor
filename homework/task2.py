"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque
print("Программа для определения суммы и произведения заданных шестнадцатеричных чисел")
definition = {'0': 0,
              '1': 1,
              '2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              'A': 10,
              'B': 11,
              'C': 12,
              'D': 13,
              'E': 14,
              'F': 15}

first = (input('Введите первое целое шестнадцатеричное число: ').upper())
second = (input('Введите первое целое шестнадцатеричное число: ').upper())
first_list = []
second_list = []
result = deque()
for a in first:
    first_list += a
for a in second:
    second_list += a
print(first_list)
print(second_list)
while len(first_list) < len(second_list):
    first_list.insert(0, 0)
    first_list[0] = str(first_list[0])
print(first_list)
print(second_list)

a = definition[first_list[-1]] + definition[second_list[-1]]
while len(first_list) > 0:
    a = definition[first_list[-1]] + definition[second_list[-1]]
    count = 0
    if a > 15:
        count += a // 16
        a = a % 16
        definition[first_list[-2]] += count
    result.appendleft(a)
    first_list.pop(-1)
    second_list.pop(-1)
print(result)
"""
while len(first_list) > 0:
    a = definition[first_list[-1]] + definition[second_list[-1]]
    count = 0
    if a > 15:
        count += a // 15 
        a = a % 15
        definition[first_list[-2]] = definition[first_list[-2]]+ count
        result.appendleft(a)
    result.appendleft(a)
    first_list.pop(-1)
    second_list.pop(-1)
print(result)
"""