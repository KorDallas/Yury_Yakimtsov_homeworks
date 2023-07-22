# Ввести 10 чисел с клавиатуры, данные числа добавить во множество.

approach = 10
set_result = set()
while approach != 0:
    num = int(input('Введите число: '))
    set_result.add(num)
    approach -= 1
print('Множество из введённых чисел''\n', f'{set_result}')
