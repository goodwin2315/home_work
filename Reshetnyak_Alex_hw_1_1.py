
duration = int(input('ведите значение в секундах: '))
seconds = duration % (24 * 3600 * 86400)
day = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print('%03d:%02d:%02d:%02d' % (day, hours, minutes, seconds))
