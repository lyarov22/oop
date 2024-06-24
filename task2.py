#task2.py
# Task4. Из трех данных чисел выбрать наименьшее и наибольшее.

def find_min_max(a, b, c):
    numbers = [a, b, c]
    min_number = min(numbers)
    max_number = max(numbers)
    return min_number, max_number

# Пример использования функции
a, b, c = 5, -1, 12
min_num, max_num = find_min_max(a, b, c)
print(f"Наименьшее число: {min_num}, наибольшее число: {max_num}")  # Вывод: Наименьшее число: -1, наибольшее число: 12
