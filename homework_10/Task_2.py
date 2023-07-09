# Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами.
# Выведите полученный словарь на экран.

method_1 = dict.fromkeys(['1', '2', '3'], 0)
print(method_1)
lst1 = ['1', '2', '3']
lst2 = [0, 0, 0]
method_2 = dict(zip(lst1, lst2))
print(method_2)
method_3 = {key: 0 for key in lst1}
print(method_3)
