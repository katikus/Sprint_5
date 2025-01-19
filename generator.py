import random

def generate_email(first_name: str = 'Nikita', last_name: str = 'Nikulochkin', domain: str = "yandex.ru", kagorta: str = '17') -> str:
    # Преобразуем имена в нижний регистр и удаляем пробелы
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()

    # Генерация email по паттерну
    email = f"{first_name}{last_name}{kagorta}{random.randint(1, 999)}@{domain}"

    return email