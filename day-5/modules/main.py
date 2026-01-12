from symbols import is_vowel

def count_vowels(text):
    count = 0
    for char in text:
        if is_vowel(char):
            count += 1
    return count