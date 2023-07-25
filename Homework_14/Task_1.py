# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль” Ноль использовать в качестве завершения программы
# (сделать как отдельную операцию).

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        return None


while True:
    num1 = float(input('Первое число: '))
    num2 = float(input('Второе число: '))
    operation = input("Введите действие или нажмите 0 для завершения: ")
    if operation == '-':
        print(subtract(num1, num2))
    elif operation == '+':
        print(add(num1, num2))
    elif operation == '*':
        print(multiply(num1, num2))
    elif operation == '/':
        print(divide(num1, num2))
    elif operation == '0':
        print("Программа завершена. ")
        break
    else:
        print("Не верный ввод данных")
