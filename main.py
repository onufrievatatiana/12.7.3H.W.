per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
values = list(per_cent.values())
deposit = (round(values[0]*money), round(values[1]*money), round(values[2]*money), round(values[3]*money))
print('deposit = ', deposit)
print('deposit i = ', max(deposit))
