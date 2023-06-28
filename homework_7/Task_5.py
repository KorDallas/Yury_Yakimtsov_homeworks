# Заполните список ста нулями, кроме первого и последнего элементов, они дожни быть равны единице.

list_1 = [0 for i in range(100)]
index_list = list_1.index(0)
list_1[index_list] = 1
list_1.sort()
index_list = list_1.index(0)
list_1[index_list] = 1
print(list_1)  # Весь список 100 нулей, первый и последний элемент = 1
print(len(list_1))  # длинна списка
