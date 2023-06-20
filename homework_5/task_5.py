# Есть список чисел с дубликатами. Создать новый список в котором будут только уникальные элементы.

list1 = [1, 2, 2, 3, 1, 4, 4, 5, 1, 5, 5, 6, 6, 6]
list2 = []

for i in list1:
    if list1.count(i) and i not in list2:
       list2.append(i)

print(list2)