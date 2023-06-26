# Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно
# в порядке возрастания, если m < n, или в порядке убывания если наоборот.

m = int(input("Введите первое целое число: "))
n = int(input("Введите второе целое число: "))
# Первый способ

# if m < n:
#     list_mn = [i for i in range(m, n + 1)]
#     for i in list_mn:
#         print(i)
# elif m > n:
#     list_mn = [i for i in range(m, n - 1, -1)]
#     for i in list_mn:
#         print(i)
# else:
#     print(f'Значения m и n = {m}')

# Второй способ
if m < n:
    num = -1
    num += m
    while num < n:
        num += 1
        print(num)
else:
    num = 1
    num += m
    while num > n:
        num -= 1
        print(num)
