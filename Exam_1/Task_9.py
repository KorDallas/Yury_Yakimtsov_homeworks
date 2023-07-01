# Дан список [student1, student2, student3] с помощью цикла for
# добавить к каждому элементу списка слово " good".
# Вывести на экран.
student1 = input("Первый студент: ")
student2 = input("Второй студент: ")
student3 = input("Третий студент: ")
list1 = [student1, student2, student3]
print(f'Основной список {list1}')
word = " good"
index_lis1 = ()
for i in list1:
    index_list1 = list1.index(i)
    list1[index_list1] = i + word
print('Новый список с добавлением слова " good": ', f'{list1}', sep='\n')
