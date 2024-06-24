#task4.py
# 4.Ввести с клавиатуры значения трех сторон треугольника a, b и c и определить, является ли он прямоугольным. Ответ вывести в виде сообщения.
def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "Треугольник является прямоугольным."
    else:
        return "Треугольник не является прямоугольным."

# Пример использования функции
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
result = is_right_triangle(a, b, c)
print(result)