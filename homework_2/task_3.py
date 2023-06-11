string = input('Введите строку:')
string_m = int(len(string)) % 3
if string_m == 0:
    print(string + "!")
else:
    print("Количество символов в строке не кратно трём")