def count_chars(text,char):
    text_lower = text.lower()
    char_lower = char.lower()
    return text_lower.count(char_lower)

print(count_chars('HexlEt','e'))
print(count_chars('HexlEt','E'))