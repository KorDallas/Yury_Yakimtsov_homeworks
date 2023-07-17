# Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация, то есть соединение, строк.
# В остальных случаях введенные числа суммируются.
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
while True:
    First_line = input('Введите данные: ')
    if First_line == '':
        print('Работа программы завершена')
        break
    Second_line = input('Введите данные: ')
    if is_number(First_line) and is_number(Second_line) == True:
        print(float(First_line) + float(Second_line))
    else:
        print(First_line + Second_line)
