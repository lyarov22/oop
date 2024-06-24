#task13.py
# 13. Дан массив размера N. Вывести его элементы в обратном порядке. 
def reverse_array(arr):
    reversed_arr = arr[::-1]
    return reversed_arr

# Пример использования функции
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print("Массив в обратном порядке:", reversed_arr)
