# Дезоксирибонуклеиновая кислота (ДНК) представляет собой химическое вещество, находящееся в ядре клеток
# и несущее (инструкции) по развитию и функционированию животных организмов.
# В цепочке ДНК символы "А" и "Т" дополняют друг друга, как "С" и "G".
# Вам нужно вернуть другую дополнительную сторону.
# Нить ДНК никогда не бывает пустой или ДНК вообще не существует. Пример: (ввод --> вывод)
# "ATTGC" --> "TAACG"
# 'GTAT' --> 'CATA'

# Для решения данной задачи я использовал случайно сгенерированную последовательность, т.к. способ получения
# подобных данных уже был в предыдущей задаче но ручной ввод закоментирован. В данном случаем пользователю просто нужно указать длину последовательности и программа все сгенерирует
# и выдаст ответ.

import random
length = int(input("Введите длину последовательности ДНК: "))
dna_list = "ATCG"
dna_char_list = ['A', 'T', 'C', 'G']
dna_char_list2 = ['T', 'A', 'G', 'C']
dna_list_map = dict(zip(dna_char_list, dna_char_list2))
dna_line = ''.join(random.choice(dna_list) for i in range(length))
mapping = lambda line: ''.join(dna_list_map[x] for x in line)
# dna_inp = input("Введите последовательность ДНК состоящую из символов 'A, T, C, G': ")
# dna_inp = dna_inp.upper()
# flag = True
# for i in dna_inp:
#     if i not in dna_list:
#         flag = False
#         break
# if flag:
#     print(f'Исходная последовательность ДНК: {dna_line}')
#     print(f' Другая сторона исходной последовательности ДНК {mapping(dna_line)}')
# else:
#     print("Последовательности ДНК не существует, повторите.")
print(f'Исходная последовательность ДНК: {dna_line}')
print(f' Другая сторона исходной последовательности ДНК {mapping(dna_line)}')
