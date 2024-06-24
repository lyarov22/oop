#task8.py
# 8. Даны два целых числа A и B (A < B). Вывести все целые числа, расположенные между данными числами (включая сами эти числа), в порядке их возрастания, а также количество N этих чисел. 
def print_numbers_and_count(a, b):
    if a >= b:
        return "Ошибка: A должно быть меньше B."
    
    numbers = list(range(a, b + 1))
    count = len(numbers)
    
    print("Числа между A и B (включительно):")
    for number in numbers:
        print(number, end=' ')
    
    print(f"\nКоличество этих чисел: {count}")
    return count

# Пример использования функции
a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B: "))
print_numbers_and_count(a, b)
