# Даны два целых числа m и n.
# Напишите программу, которая выводит все числа от m до n если m < n в порядке возрастания
# или в порядке убывания если m > n.

m = int(input("Введите первое целое число: "))
n = int(input("Введите второе целое число: "))

if m < n:
    for i in range(m, n+1):
        print(i)
elif m > n:
    for i in range(m, n-1, -1):
        print(i)
