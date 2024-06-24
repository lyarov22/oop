#task17.py
# 17. Построить строку, состоящую из малых букв латинского алфавита (по
#алфавиту).
import string

def lowercase_alphabet_string():
    alphabet = string.ascii_lowercase
    return alphabet

# Example usage
alphabet_string = lowercase_alphabet_string()
print("String of lowercase letters:", alphabet_string)
