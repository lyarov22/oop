#task7.py
# 7. Даны натуральные числа х и у. Вычислить произведение , используя лишь операцию сложения. Задачу решить двумя способами x y

def multiply_using_addition_recursive(x, y):
    if y == 0:
        return 0
    return x + multiply_using_addition_recursive(x, y - 1)

# Пример использования функции
x = int(input("Введите натуральное число x: "))
y = int(input("Введите натуральное число y: "))
result = multiply_using_addition_recursive(x, y)
print(f"Произведение {x} и {y} равно {result}")
