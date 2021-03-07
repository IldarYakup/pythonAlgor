"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
"""
https://drive.google.com/file/d/1S61A6uOFO3_YSilFb_aNRE7skTcVE5N3/view?usp=sharing
"""
def reverse(a):
    i = len(str(a))
    final = 0
    while i > 0:
        num = a % 10
        a = (a - num) / 10
        a = int(a)
        final = final + num * 10 ** (i - 1)
        i -= 1
    return final


print("Программа для вывода обратного порядка цифр заданного числа")
user_number = int(input("Введите натуральное число, для обратного порядка цифр: "))
print(reverse(user_number))
