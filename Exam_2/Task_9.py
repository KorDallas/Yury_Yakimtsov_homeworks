# Джейден Смит, сын Уила Смита, является звездой таких фильмов, как "Каратэ-пацан" (2010) и "После Земли" (2013).
# Джейден так же известен своей философией, которую он распространяет через Twitter.
# Когда он пишет в твиттере, он почти всегда пишет каждое слово с большой буквы.
# Для простоты вам придётся писать каждое слово с заглавной буквы.
# Посмотрите, какими должны быть сокращения в приведенном ниже примере.
# Ваша задача состоит в том, чтобы преобразовать строки в то, как они были бы написны Джеденом Смитом.
# Строки являются настоящими цитатами Джейдена Смита, но они не написаны с заглавной буквы так, как он их
# изначально напечатал.

# Пример:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased: "How Can Mirrors Be Real If Our Eyes Aren't Real"

import re
string = "How can mirrors be real if our eyes aren't real"
Jaden_translater = input('Enter your text: ')

# Нашёл в интернете решение проблемы с апострофами
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
     lambda mo: mo.group(0)[0].upper() +
     mo.group(0)[1:].lower(),
     s)


print(titlecase(Jaden_translater))
print(string.title())
