# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.

with open('task_1_file.txt', 'w') as file:
     file.write('hello world\n'
                '1\n'
                '2\n'
                'good\n'
                'mood\n'
                '12\n'
                '666\n'
                'ok\n'
                '13_to\n'
                'hi\n'
                '1888'
                )
with open('task_1_file.txt', 'r') as file:
    list1 = file.read().split('\n')
print(list1)
list_digit = []
list_string = []
for i in list1:
    if i.isdigit():
        list_digit.append(int(i))
    else:
        list_string.append(i)
print(sorted(list_digit) + sorted(list_string, key=len))
