# Напишите программу, которая подключает модуль math и используя значение числа \pi
# из этого модуля, вводим радиус круга и находим периметр этого круга, результат вывести на экран.

import math
R = int(input('Введите радиус окружности: '))
print(f'Периметр искомой окружности = {2 * math.pi * R}')
