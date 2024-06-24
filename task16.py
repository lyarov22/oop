#task16.py
# 16. Дана строка S и число N. Преобразовать строку S в строку длины N следующим образом: если длина строки S больше N, то отбросить первые символы, если длина строки S меньше N, то в ее начало добавить символы "." (точка). 

def transform_string(S, N):
    if len(S) > N:
        transformed_string = S[-N:]  # Отбрасываем первые символы, если длина S больше N
    elif len(S) < N:
        transformed_string = '.' * (N - len(S)) + S  # Добавляем точки в начало, если длина S меньше N
    else:
        transformed_string = S  # Если длина S равна N, строка остается без изменений
    
    return transformed_string

# Пример использования функции
S = "Hello"
N = 8
result = transform_string(S, N)
print(f"Преобразованная строка: '{result}'")
