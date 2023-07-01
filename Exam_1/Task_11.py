# Дана строка ["hello my friend", "my name is", "house", "cat", "dog"].
# В новый список добавить элементы которые содержат пробел.

list_1 = ["hello my friend", "my name is", "house", "cat", "dog"]
check_space = " "
new_list = []
for i in list_1:
    if i.find(check_space) != -1:
        new_list.append(i)
print(new_list)
