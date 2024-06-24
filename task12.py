#task12.py
# 12. Напишите метод, заменяющий в строке все вхождения слова «бяка» на «вырезано цензурой».
def censor_word(text):
    censored_text = text.replace("бяка", "вырезано цензурой")
    return censored_text

# Пример использования функции
input_text = input("Введите строку для цензуры: ")
result = censor_word(input_text)
print(f"Цензурированный текст: {result}")
