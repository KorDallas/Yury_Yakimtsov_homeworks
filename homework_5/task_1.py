# Перемножить все нечётные значения в диапазоне от 1 до 100.

num = 1
for i in range(1, 100):
    if i % 2 != 0:
         num *= i
print(num)