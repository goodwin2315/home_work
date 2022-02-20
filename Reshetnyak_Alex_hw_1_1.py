
duration = int(input('ведите значение в секундах: '))
seconds = duration % (24 * 3600 * 86400)
day = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
if duration < 60:
    print(f'{seconds} сек')
if 3600 > duration > 60:
    print(f'{minutes} мин {seconds} сек')
if 3600 < duration < 86400:
    print(f'{hours} час {minutes} мин {seconds} сек')

