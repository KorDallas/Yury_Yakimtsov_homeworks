# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

import random
arr_min = int(input("Введите минимальную границу массива: "))
arr_max = int(input("Введите максимальную границу массива: "))
arr_len = int(input("Введите длину массива: "))
arr_main = [random.randint(arr_min, arr_max) for i in range(arr_len)]
print('Исходный массив: ', '\n' f'{arr_main}')
print('Введите удаляемый диапазон!')
del_min = int(input('Введите минимальную границу: '))
del_max = int(input('Введите максимальную границу: '))
i = 0
count = arr_len
while i < count:
    if del_min <= arr_main[i] <= del_max:
        del arr_main[i]
        count -= 1
    else:
        i += 1
for i in range(count, arr_len):
    arr_main.append(0)
print(f'Новый массив {arr_main}')

