#task15.py
# 15. а).Tkinter.Создать форму произвольного размера
#б).На этой форме разместить следующие элементы:
#a)Button
#b)Label
#c)Entry
#в).Каждый элемент имеет свою цветовую характеристику(фон,текст)
#г).Обработать нажатие или выбор для каждого элемента выдав
#соответствующее сообщение.

import tkinter as tk
from tkinter import messagebox

def button_clicked():
    messagebox.showinfo("Сообщение", "Кнопка была нажата!")

def entry_return(event):
    entry_text = entry.get()
    messagebox.showinfo("Введен текст", f"Текст из Entry: {entry_text}")

# Создание главного окна
root = tk.Tk()
root.title("Пример формы с элементами Tkinter")
root.geometry("400x300")  # Устанавливаем размеры окна

# Создание кнопки
button = tk.Button(root, text="Нажми меня", bg="blue", fg="white", command=button_clicked)
button.pack(pady=20)

# Создание метки
label = tk.Label(root, text="Пример метки", bg="green", fg="white")
label.pack()

# Создание поля ввода
entry = tk.Entry(root, bg="yellow", fg="black")
entry.pack(pady=10)

# Привязка события для поля ввода (нажатие Enter)
entry.bind("<Return>", entry_return)

# Запуск главного цикла обработки событий
root.mainloop()
