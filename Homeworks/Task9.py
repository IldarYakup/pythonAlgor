"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
def max_summ(a, b, c):
    def summ(a):
        i = len(str(a))
        final_num=0
        while i >= 1:
            sum_num = a // 10**(i-1)
            a = a - sum_num*10**(i-1)
            i -= 1
            final_num += sum_num
        return final_num
    if summ(a)>summ(b) and summ(a)>summ(b):
        print(f'натуральное число {a} с суммой чисел {summ(a)} наибольшее')
    elif summ(b) > summ(a) and summ(b) > summ(c):
        print(f'натуральное число {b} с суммой чисел {summ(b)} наибольшее')
    elif summ(c) > summ(a) and summ(c) > summ(b):
        print(f'натуральное число {c} с суммой чисел {summ(c)} наибольшее')
    else:
        print(f'Суммы нескольких из введенных натуральных чисел равны.')

print("Программа для определения натурального числа, в котором наибольшая сумма цифр")
first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
third_num = int(input("Введите третье число: "))

max_summ(first_num, second_num, third_num)