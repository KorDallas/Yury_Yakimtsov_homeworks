# В классе N школьников. На уроке физкультуры тренер говорит "На первый-второй рассчитайтесь".
# Выведите, что скажут ученики.
# Входные данные: Вводится целое число - кол-во человек в классе.
# Выходные данные: Выведите последовательность чисел 1 и 2, в том порядке, как будут говорить школьники.

p_num = int(input("Введите кол-во учеников на уроке: "))
check = 2
while p_num > 1:
    print(1)
    print(2)
    p_num -= 2
    if p_num == 1:
        print(1)