def count_vowels(text):
    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

print(f"'Hello, World!' -> {count_vowels('Hello, World!')}") # Ожидаем 3
print(f"'Python' -> {count_vowels('Python')}")         # Ожидаем 1
print(f"'BCDFG' -> {count_vowels('BCDFG')}")          # Ожидаем 0
print(f"'AEIOUaeiou' -> {count_vowels('AEIOUaeiou')}")