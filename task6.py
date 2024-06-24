#task6.py
# 6.Дана длина окружности. Найти площадь круга, ограниченного этой окружностью. В качестве значения Pi использовать 3.14. 

def circle_area_by_circumference(circumference):
    pi = 3.14
    radius = circumference / (2 * pi)
    area = pi * (radius ** 2)
    return area

# Пример использования функции
circumference = float(input("Введите длину окружности: "))
area = circle_area_by_circumference(circumference)
print(f"Площадь круга: {area}")
