# Необходимо удалить пустые строки из списка строк.

list1 = [' ', 'abc', 'bca', '    ', " ", "     ", 'aaa']
new_list = []
for i in list1:
    if not i.isspace():
        new_list.append(i)
list1 = new_list
print(f'Список без пустых строк: {list1}')