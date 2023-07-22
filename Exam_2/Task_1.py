# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt. После этого удалите созданную папку.
#  Все операции выполнять с помощью встроенных функций библиотеки os.

import os
os.mkdir('C:\\Users\Iryna\Desktop\Test')
os.chdir('C:\\Users\Iryna\Desktop\Test')
with open('test_1.txt', 'w') as file:
    file.write('')
with open('test_2.txt', 'w') as file:
    file.write('')
with open('test_3.txt', 'w') as file:
    file.write('')
os.rename("test_1.txt", "rename_1.txt")
os.rename("test_2.txt", "rename_2.txt")
os.rename("test_3.txt", "rename_3.txt")
os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir('..')
os.rmdir('C:\\Users\Iryna\Desktop\Test')
