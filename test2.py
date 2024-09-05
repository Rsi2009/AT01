import pytest
from main2 import count_vowels

def test_count_vowels():
    # Список тестов: каждый элемент - это кортеж (строка, ожидаемый результат)
    test_cases = [
        ("aeiou", 5),  # Только гласные
        ("АЕЁИОУЫЭЮЯ", 10),  # Только гласные (русские)
        ("bcdfghjklmnpqrstvwxyz", 0),  # Без гласных
        ("1234567890", 0),  # Без букв
        ("Hello, World!", 3),  # Смешанная строка
        ("Мама мыла раму", 6),  # Смешанная строка (русская)
        ("AEIOU and some consonants", 9),  # Смешанная строка
        ("Привет, как дела?", 6),  # Смешанная строка (русская)
    ]

    # Проходим по всем тестовым случаям
    all_tests_passed = True
    for input_str, expected in test_cases:
        result = count_vowels(input_str)
        if result == expected:
            print(f"Тест пройден: {input_str} -> {result}")
        else:
            print(f"Тест не пройден: {input_str} -> {result} (ожидалось {expected})")
            all_tests_passed = False

    # Проверка всех тестов
    if all_tests_passed:
        print("Все тесты пройдены.")
    else:
        print("Некоторые тесты не пройдены.")

# Запуск тестов
test_count_vowels()


# Запуск тестов
test_count_vowels()