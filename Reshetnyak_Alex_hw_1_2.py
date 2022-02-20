pow_odd_numbers = [i ** 3 for i in range(1, 1000, 2)]

number_1 = 0
number_2 = 0
sum_number = []
for elem in range(len(pow_odd_numbers)):
    number = 0
    i = pow_odd_numbers[elem]
    while i > 0:
        digit = i % 10
        number = number + digit
        i = i // 10
    if number % 7 == 0:
        number_1 += pow_odd_numbers[elem]
    pow_odd_numbers[elem] += 17
    number = 0
    i = pow_odd_numbers[elem]
    while i > 0:
        digit = i % 10
        number = number + digit
        i = i // 10
    if number % 7 == 0:
        number_2 += pow_odd_numbers[elem]
print(number_1)
print(number_2)
