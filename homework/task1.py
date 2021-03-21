"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter

user_company = int(input("Введите количество предприятий: "))
list_dict = []
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
               }
    list_dict.append(company)
profit = Counter()
for company in list_dict:
    profit_comp = company.copy()
    del profit_comp['name']
    profit += Counter(profit_comp)
average = sum(profit.values())/user_company
print(f'Среднегодовая прибыль между всему предприятиями равна {average}')
most_avr = []
least_avr = []
avr = []
for i, company in enumerate(list_dict):
    avr_company = company["I квартал"] + company["II квартал"] + company["III квартал"] + company["IV квартал"]
    if avr_company < average:
        least_avr += [[company["name"], avr_company]]
    elif avr_company > average:
        most_avr += [[company["name"], avr_company]]
    else:
        avr = company["name"]

for a in most_avr:
    print(f'Предприятия {a[0]} со среднегодовой прибылью {a[1]} выше среднего показателя всех предприятий')
for a in avr:
    print(f'Прибыль предприятия {a} равна среднегодовой прибыли всех предприятий')
for a in least_avr:
    print(f'Предприятия {a[0]} со среднегодовой прибылью {a[1]} ниже среднего показателя всех предприятий')

