# Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт.
# (целое число). Напишите программу, подсчитывающую общую стоимость заказа.


with open('Task_4_list.txt', 'w', encoding='utf-8') as file:
    lines = file.writelines(
        ['Полка\t', '3\t', '9.95\t\n',
         'Шкаф\t', '1\t', '56.95\t\n',
         'Стул\t', '4\t', '12.95\t\n',
         'Кресло\t', '2\t', '34.95\t']
        )

with open('Task_4_list.txt', 'r', encoding='utf-8') as file:
    total_cost = 0
    while True:
        a = file.readline().split()
        if a == []:
            break
        print(f'{a[0]}  {a[1]} шт.  {a[2]} руб.')
        total_cost += (int(a[1]) * float(a[2]))
print(f'Общая стоимость товаров в чеке составляет {total_cost} руб.')
