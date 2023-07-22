# Создайте словарь из строки 'An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

my_string = 'An apple a day keeps the doctor away'
dct_solution = {key: my_string.count(key) for key in my_string}
print(f'Словарь где ключи это символы строки, а значения это кол-во этих символов в строке:', '\n' f'{dct_solution}')
# without ' '
new_mystring = my_string.replace(' ', '')
dct_solution2 = {key: new_mystring.count(key) for key in new_mystring}
print(f'Словарь где ключи это символы строки (только буквы):', '\n' f'{dct_solution2}')
