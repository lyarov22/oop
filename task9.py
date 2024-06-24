#task9.py
# 9.В заданной строке посчитать количество русских букв «А».
def count_letter_a(text):
    count = 0
    for char in text:
        if char == 'А' or char == 'а':  # учитываем и заглавные, и строчные буквы
            count += 1
    return count

# Пример использования функции
input_text = input("Введите строку для подсчета букв 'А': ")
result = count_letter_a(input_text)
print(f"Количество букв 'А' в строке: {result}")
