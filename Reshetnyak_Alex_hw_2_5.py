list1 = [57.8, 46.51, 97]
fix_prices = []
for el in list1:
    rub = int(el)
    kopek = round((el - rub) * 100)
    fix_prices.append(f'{rub} руб {kopek:02d} коп')
print((', '.join(fix_prices)))
id_new = id(list1)
print(id_new)
list1.sort()
print(list1)
new_list = sorted(list1, reverse=True)
print(new_list)
