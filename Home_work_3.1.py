from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Отримання поточної дати
        today = datetime.now().date()

        # Розрахунок різниці між поточною датою та заданою датою
        days_difference = (today - date_obj).days
        
        return days_difference
    
    except ValueError:
        return "Некоректний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

# Приклад використання функції
current_date = datetime.now().strftime('%Y-%m-%d')
print(f"Сьогоднішня дата: {current_date}")
print(f"Кількість днів до 9 жовтня 2021 року: {get_days_from_today('2021-10-09')}")
