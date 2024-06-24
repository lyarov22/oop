#task10.py
# 10.В заданной строке удалить второй и четвертый по счету символы.
def remove_characters(string):
    if len(string) < 5:  # проверяем, что строка достаточно длинная для удаления второго и четвертого символов
        return "Ошибка: Строка должна быть длиннее 4 символов."
    
    modified_string = string[:1] + string[2:3] + string[4:]  # формируем строку без второго и четвертого символов
    
    return modified_string

# Пример использования функции
input_string = input("Введите строку для удаления второго и четвертого символов: ")
result = remove_characters(input_string)
print(f"Модифицированная строка: {result}")
