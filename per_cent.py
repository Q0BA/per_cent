per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = input('Введите сумму зачисляемую на счёт: ')

per_cent_list = list(map(float, per_cent.values()))
print(per_cent_list)
