import random

def choice_from_range(text,start,end):
    random_index = random.randint(start,end)
    return text[random_index]
text = "abcdef"

print(choice_from_range(text, 3, 5))  # может вернуть 'd', 'e' или 'f'
print(choice_from_range(text, 3, 5))  # может вернуть 'd', 'e' или 'f'
print(choice_from_range(text, 3, 5))  # может вернуть 'd', 'e' или 'f'
print(choice_from_range(text, 2, 2))  # всегда вернет 'c'
print(choice_from_range(text, 0, 2))  