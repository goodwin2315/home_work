pow_odd_numbers = [i ** 3 for i in range(1, 1000, 2)]
number = 0
number_1 = 0
sum_number = []
sum_17 = []
for elem in pow_odd_numbers:
    while elem > 0:
        digit = elem % 10
        number = number + digit
        elem = elem // 10
    if number % 7 == 0:
        sum_number.append(number)
    else:
        number = 0
for el in sum_number:
    el = el + 17
    while el > 0:
        digit = el % 10
        number_1 = number_1 + digit
        el = el // 10
    if number_1 % 7 == 0:
        sum_17.append(number_1)
    else:
        number_1 = 0
print(f'Сумма тех чисел из этого списка, сумма цифр которых делится нацело на 7 равна: {sum(sum_number)}')
print(f'Сумма тех чисел из этого списка + 17, сумма цифр которых делится нацело на 7 равна: {sum(sum_17)}')

