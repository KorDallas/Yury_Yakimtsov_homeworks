# Если в функцию передается кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нем.
# Число - количество нечетных цифр. Строка - количество букв.


def words_len_sum(tuple1):
    length = 0
    for word in tuple1:
        if type(word) == str:
            length += len(word)

    return length


def char_and_num(str_list):
    number_of_letters = 0
    number_of_odd_numbers = 0
    for elem in str_list:
        if isinstance(elem, str):
            number_of_letters += len(elem)
        elif isinstance(elem, int):
            if elem % 2 != 0:
                number_of_odd_numbers += 1

    return number_of_letters, number_of_odd_numbers


list1 = ['a', 4, 'b', 'df', 7, 99, 0]
tuple1 = ('asaf', 66, 'dsfefg', 'u', 7)
print(words_len_sum(tuple1))
print(char_and_num(list1))
