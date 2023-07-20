# Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов(вывести имя папки и имена файлов)

import os

os.chdir(r'C:\Users\Iryna\PycharmProjects\homework_13\direct')
print(os.listdir(r'C:\Users\Iryna\PycharmProjects\homework_13\direct'))
for dirpath, dirnames, filenames in os.walk("."):
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
