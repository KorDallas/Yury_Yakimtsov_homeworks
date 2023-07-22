# Найти в списке те элементы,
# значение которых меньше среднего арифметического, взятого от всех элементов списка.
import random

import random
list_task = [random.randint(1, 20) for i in range(15)]
list_of_solution = []
print(f'Исходный список {list_task}')
aver_list = sum(list_task) / len(list_task)
print(f'Среднеарифметическое исходного списка списка {aver_list}')
for i in list_task:
    if i < aver_list:
        list_of_solution.append(i)
print(f'Список значение которых меньше среднего арифметического {list_of_solution}')
