# Обозначьте порядок вычисления выражения по операциям 11*2**2-13/4+7.
# Какое число получилось?
act = 2**2 # первое действие возведение в степень
act_2 = 11 * act # второе действие умножение
act_3 = 13 / 4 # действие 3 деление
act_4 = act_2 - act_3 # четвёртое действие будет вычитание по смыслу выражения
act_5 = act_4 + 7 # пятое действие сложение по смыслу выражения
print(act_5)