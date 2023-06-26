# Даны несколько списков: [-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
# Для каждого из списков найти второе наименьшее значение в нем.

# Первый способ
# new_list = []
list1 = [-8, 1, 2, -2, 0]
# new_list = sorted(list1)
# print(f'Второе наименьшее значение списка {list1} это {new_list[1]}')
list2 = [1, -1, 0, -9, 4, -5]
# new_list = sorted(list2)
# print(f'Второе наименьшее значение списка {list2} это {new_list[1]}')
list3 = [1, 4, 0, 23, 6, 34]
# new_list = sorted(list3)
# print(f'Второе наименьшее значение списка {list3} это {new_list[1]}')

# Второй способ (самый чёткий)

list_of_lists = [list1, list2, list3]
for i in list_of_lists:
    i.sort()
    print(i[1])

# Третий способ

# list4 = []
# list4.append(list1)
# list4.append(list2)
# list4.append(list3)
# temp = 0
# for i in list4:
#     temp = i
#     temp.sort()
#     print(temp[1])
