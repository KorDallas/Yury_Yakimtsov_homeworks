# Заполните список ста нулями, кроме первого и последнего элементов, они дожни быть равны единице.

list_1 = [0 for i in range(100)]
list_1[0] = 1
list_1[99] = 1
print(list_1)  # Весь список 100 нулей, первый и последний элемент = 1
print(len(list_1))  # длинна списка
