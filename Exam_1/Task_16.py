# Напишите программу, которая вычисляет процентное содержание символов G(гуанин) и C(цитозин) во введённой строке
# (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10*100 = 40.
# Где 4 - это кол-во символов G и C, а 10 - это длинна строки.

list_of_nucleo = 'acgtu'
gc_sum = 0
flag = True
list1 = input("Введите последовательность цепочки 'a c g t u': ")
list1 = list1.lower()
for i in list1:
    if i == 'g' or i == 'c':
        gc_sum += 1
    elif i not in list_of_nucleo:
        flag = False
        break
gc_percent = gc_sum / len(list1) * 100
if flag:
    print(f'Процентное содержание символов G и C равно: {round(gc_percent, 2)}')
else:
    print("Некорректный ввод цепочки")
