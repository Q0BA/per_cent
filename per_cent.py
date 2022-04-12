per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input('Введите сумму зачисляемую на счёт: '))

per_cent_list = list(map(float, per_cent.values()))

bank1 = money*per_cent_list[0]/100
bank2 = money*per_cent_list[1]/100
bank3 = money*per_cent_list[2]/100
bank4 = money*per_cent_list[3]/100

deposit = [bank1,bank2,bank3,bank4]

print("Максимальная сумма, которую вы можете заработать — ",max(deposit))
