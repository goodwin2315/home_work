list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for i in list1:
    if i.isdigit():
        new_list.extend(['"', i.zfill(2), '"'])
    elif i[1:].isdigit() and i[0:] == '-' or i[0:] == '+':
        new_list.extend(['"', i.zfill(3), '"'])
    else:
        new_list.append(i)
print(' '.join(new_list))
