# Функция для вывода таблицы умножения для указанного числа.

def mult_table(number):
    print("Таблица умножения числа", number)
    for i in range(1, 11):
        print(number, 'x', i, '=', number * i)



number = int(input("Введите число: "))
if type(number) == int:
    print(mult_table(number))
else:
    print("Ошибка ввода!")
    