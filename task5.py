#task5.py
# 5.Найти периметр и площадь прямоугольного треугольника, если даны длины его катетов a и b. 
import math

def right_triangle_properties(a, b):
    # Вычисление гипотенузы
    c = math.sqrt(a**2 + b**2)
    
    # Вычисление периметра
    perimeter = a + b + c
    
    # Вычисление площади
    area = 0.5 * a * b
    
    return perimeter, area

# Пример использования функции
a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))
perimeter, area = right_triangle_properties(a, b)
print(f"Периметр прямоугольного треугольника: {perimeter}")
print(f"Площадь прямоугольного треугольника: {area}")
