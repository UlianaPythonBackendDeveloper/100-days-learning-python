text = 'If I look back I am lost'

def filter_string(text,char_to_remove):
    result = ""
    for current_char  in text:
        if current_char != char_to_remove:
            result += current_char
            
    return result
print(filter_string(text, 'I'))
print(filter_string(text, 'o'))