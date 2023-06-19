# Определить существование треугольника, а так же определить его тип.

side1 = int(input("Введите длинну первой стороны: "))
side2 = int(input("Введите второй первой стороны: "))
side3 = int(input("Введите второй третьей стороны: "))
a = side1 * side1
b = side2 * side2
c = side3 * side3

if side1 == side2 == side3:
    print("Есть равносторонний треугольник")
elif (side1 == side2 != side3) or (side2 == side3 != side1) or (side1 == side3 != side2):
    print("Есть равнобедренный треугольник")
elif a + b == c or a + c == b or b + c == a:
    print("Есть прямоугольный треугольник")
else:
    print("Треугольник не обнаружен")
