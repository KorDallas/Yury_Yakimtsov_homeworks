# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

def longest_word(file):
    with open('article.txt', 'r', encoding='utf-8') as file:
        words = file.read().split()  #'/n' в метод split для поиска самой длинной строки, а не слов.
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print('Самое длинно слово в файле article.txt', longest_word('article.txt'))

