#
text = "When \t\n you play a \t\n game of thrones you win or you die."
print(len(text[5:15].strip()))

#
def get_hidden_card(card_number, stars_count=4):
    # Выводим последние 4 цифры карты
    last_four = card_number[-4:]
    # Формируем строку со звёздочками
    stars = '*' * stars_count
    # Возвращаем скрытый номер карты
    return stars + last_four

# def trim_and_repetitions
# BEGIN (write your solution here)
def trim_and_repeat(text,offset=0,repetitions=1):
    return text[offset:] * repetitions
# END
# def word_multiply
def word_multiply(text: str, number: int) -> str :
    return text * number

