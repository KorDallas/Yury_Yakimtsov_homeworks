# Дан список чисел. Если число встречается более двух раз, то добавить его в новый список

from random import randint
# генерируем список из 15 случайных чисел (дипозон от 0 до 30) list1

list1 = []
list2 = []

for i in range(15):
    list1.append(randint(0, 30))
# запускаем цикл счётчика значений переменной i (которая принимает значение каждого элемента цикла)
# и сравниваем с 2 списком
for i in list1:
    if list1.count(i) > 1 and i not in list2:
        list2.append(i)

print(list1)
print(list2)