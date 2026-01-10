def filter_string(text,char_to_remove):
    result_string = ""
    char_lower = char_to_remove.lower()
    
    for char in text:  
        if char.lower() != char_lower: 
            result_string += char  
    return result_string
text = 'If I look forward I win'
print(f"'{filter_string(text, 'i')}'")  # Вывод: 'f  look forward  wn'
print(f"'{filter_string(text, 'O')}'")  # Вывод: 'If I lk frward I win'
print(f"'{filter_string('Hello World', 'L')}'") # Вывод: 'Heo Word'