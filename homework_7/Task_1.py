# Дан список list=[15,48,'hello',6,19,'world']. Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр. Если не чётное, то заменить его на 1 в списке.
# Все слова: посчитать кол-во гласных и согласных. Вывести всё на экран.

list1 = [15, 48, 'hello', 6, 19, 'world']
list2 = ['a', 'e', 'o', 'i', 'u', 'y']
num1 = 0
for i in list1:
    if type(i) == int:
        if i % 2 == 0:
            print(f'Сумма цифр числа {i} равна {(i // 10) + (i % 10)}')
        elif i % 2 != 0:
            num1 = list1.index(i)
            list1[num1] = 1
print(f'Новый список с заменой нечётных чисел на 1 {list1}')
for y in list1:
    if type(y) == str:
        num1 = y
        consonant = 0
        vowel = 0
        for i in num1:
            if i in list2:
                consonant += 1
            else:
                vowel += 1
        print(f'Кол-во гласных в {num1} словах = {consonant}, согласных {vowel}')
