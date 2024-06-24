#task1.py
#Task1. Даны три целых числа. Возвести в квадрат отрицательные числа и в третью степень — положительные (число 0 не изменять).
def transform_numbers(a, b, c):
    numbers = [a, b, c]
    transformed_numbers = []

    for number in numbers:
        if number < 0:
            transformed_numbers.append(number ** 2)
        elif number > 0:
            transformed_numbers.append(number ** 3)
        else:
            transformed_numbers.append(number)
    
    return transformed_numbers

a, b, c = -2, 0, 3
print(transform_numbers(a, b, c))  # Вывод: [4, 0, 27]
