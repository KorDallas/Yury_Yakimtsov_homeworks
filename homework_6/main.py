# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифра от 1 до 10 отвечают за номера, а от 1 до 2-х за цвет (1-красный, 2-черный).
# Пользователю даётся 5 попыток угадать номер и цвет (Пример введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию

import random
step = 5
colors_list = ['красный', 'черный']
while step > 0:
    step -= 1
    colors = random.randint(1, 2)
    numbers = random.randint(1, 10)
#   print(f'{numbers} {colors}')  # Проверка
    user_num = input("Сделай ставку, ставки принимаются на красный или черный сектор от 1 до 10: ")
    user_num = user_num.split(" ")
    num_check = int(user_num[0])
    if colors == 1:
        colors = colors_list[0]
    elif colors == 2:
        colors = colors_list[1]
    if user_num[1] not in colors_list:
        print('Такого игрового сектора нет')
    elif num_check < 1 or num_check > 10:
        print('Такого игрового сектора нет')
    elif numbers != num_check or colors != user_num[1]:
        print('Ставка не сыграла')
        print(f'Выиграл номер {numbers} {colors}!')
    else:
        print('Поздравляем ваша ставка выиграла!')
