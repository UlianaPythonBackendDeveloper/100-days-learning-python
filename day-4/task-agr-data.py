def multiply_numbers_from_range(start, end):
    result = 1
    i = start
    
    while i <= end:
        result = result * i
        i = i + 1
    
    return result