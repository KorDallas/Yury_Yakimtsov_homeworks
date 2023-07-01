# Напишите программу для вычисления значения выражеий.
# Проверить правильность выполнения задания с помощью тестовых значений.

import math
alpha = float(input("Введите значение alpha: "))
beta = float(input("Введите значение beta: "))
gamma = float(input("Введите значение gamma: "))
x_1 = math.sin(alpha + beta - gamma)
x_2 = math.sin(beta + gamma - alpha)
x_3 = math.sin(gamma + alpha - beta)
x_4 = math.sin(alpha + beta + gamma)
y = 1/4 * int(x_1 + x_2 + x_3 - x_4)
print(f'Значение числа y = {y}')
