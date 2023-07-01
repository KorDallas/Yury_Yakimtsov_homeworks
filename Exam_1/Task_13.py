# Дан список чисел, необходимо удалить все вхождения числа 20 из него.

list1 = [1, 2, 20, 20, 3, 20, 20, 3, 4, 20]
temp_list = []
for i in list1:
    if i != 20:
        temp_list.append(i)
list1 = temp_list
print(list1)
