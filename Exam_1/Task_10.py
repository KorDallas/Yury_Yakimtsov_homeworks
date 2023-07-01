# выведите на экран числа от 1 до 50, кроме 35.

for i in range(1, 51):
    if i == 35:
        continue
    print(i)
