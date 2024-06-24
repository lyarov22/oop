#task14.py
# 14. Создайте массив, содержащий 10 первых нечетных чисел. Выведете элементы массива на консоль в одну строку, разделяя запятой.
def first_10_odd_numbers():
    odd_numbers = []
    count = 0
    number = 1
    
    while count < 10:
        if number % 2 != 0:
            odd_numbers.append(number)
            count += 1
        number += 1
    
    return odd_numbers

# Получение первых 10 нечетных чисел
odd_numbers = first_10_odd_numbers()

# Вывод на консоль в одну строку, разделяя запятой
print(', '.join(map(str, odd_numbers)))
