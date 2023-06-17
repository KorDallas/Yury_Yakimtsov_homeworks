def helth(level):
    if level <= 0:
        return False
    else:
        return True
print(helth(int(input("Введите уровень здоровья: "))))