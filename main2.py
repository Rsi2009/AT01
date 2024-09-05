def count_vowels(s: str) -> int:
    """Подсчитывает количество гласных в строке."""
    vowels = "aeiouаеёиоуыэюя"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count