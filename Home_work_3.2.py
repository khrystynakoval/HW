import random

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевірка валідності вхідних даних
    if not isinstance(min_val, int) or not isinstance(max_val, int) or not isinstance(quantity, int):
        return []

    if min_val < 1 or max_val > 1000 or quantity < 1 or quantity > (max_val - min_val + 1):
        return []

    # Генерування унікальних випадкових чисел
    random_numbers = random.sample(range(min_val, max_val + 1), quantity)

    # Сортування та повернення результату
    return sorted(random_numbers)

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
