#task11.py
# 11.Класс Persona содержит информацию о ФИО человека, дате рождения и адресе человека. Метод подсчитывает количество дней оставшихся до следующего дня рождения. По заданному ФИО человека узнать количество дней оставшихся до следующего дня рождения.
from datetime import datetime, timedelta

class Persona:
    def __init__(self, full_name, date_of_birth, address):
        self.full_name = full_name
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        self.address = address
    
    def days_until_next_birthday(self):
        today = datetime.now().date()
        next_birthday_year = today.year
        if today > datetime(next_birthday_year, self.date_of_birth.month, self.date_of_birth.day).date():
            next_birthday_year += 1
        next_birthday = datetime(next_birthday_year, self.date_of_birth.month, self.date_of_birth.day).date()
        days_until_birthday = (next_birthday - today).days
        return days_until_birthday

# Пример использования класса Persona
person = Persona("Иванов Иван Иванович", "1990-05-15", "г. Москва, ул. Пушкина, д. 10")
days_until_birthday = person.days_until_next_birthday()
print(f"До следующего дня рождения у {person.full_name} осталось {days_until_birthday} дней.")
