"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict

user_company = int(input("Введите количество предприятий: "))
dict = []
for i in range(user_company):
    name = input("Введите название компании: ")
    quarter_i = float(input("Введите прибыль за I квартал: "))
    quarter_ii = float(input("Введите прибыль за II квартал: "))
    quarter_iii = float(input("Введите прибыль за III квартал: "))
    quarter_iv = float(input("Введите прибыль за IV квартал: "))
    company = {"name": name,
               "I квартал": quarter_i,
               "II квартал": quarter_ii,
               "III квартал": quarter_iii,
               "IV квартал": quarter_iv,
               "Средняя прибыль": (quarter_i + quarter_ii + quarter_iii + quarter_iv)/4}
    dict.append(company)
print(dict)
