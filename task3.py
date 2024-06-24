#task3.py
# 3.Ввести с клавиатуры два числа. Определить, что больше, сумма квадратов или квадрат суммы этих чисел. Ответ вывести в виде сообщения.

def compare_squares_and_square_of_sum(x, y):
    sum_of_squares = x**2 + y**2
    square_of_sum = (x + y)**2
    
    if sum_of_squares > square_of_sum:
        return "Сумма квадратов больше квадрата суммы."
    elif sum_of_squares < square_of_sum:
        return "Квадрат суммы больше суммы квадратов."
    else:
        return "Сумма квадратов равна квадрату суммы."

# Пример использования функции
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
result = compare_squares_and_square_of_sum(x, y)
print(result)
