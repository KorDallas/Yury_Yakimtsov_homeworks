# Вам предоставляется CSV-файл, содержащий данные о продажах различных товаров.
# Каждая строка файла содержит информацию о конкретной продаже:
# название товара, количество проданных единиц и цена за единицу.
# Ваша задача - написать программу, которая считывает данные из файла и вычисляет общую сумму продаж.

import csv
products_list = [
    ['Полка', '3', '9.95'],
    ['Шкаф', '1', '56.95'],
    ['Стул', '4', '12.95'],
    ['Кресло', '2', '34.95']
]

with open('products_list.csv', 'w', newline='') as file:
    for elem in products_list:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(elem)

with open('products_list.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    total_sum = 0
    for row in reader:
        print(f'{row[0]}  {row[1]} шт.  {row[2]} руб.')
        total_sum += (int(row[1]) * float(row[2]))
print(f'Общая стоимость за товар составила {total_sum} руб.')
