def get_same_parity(numbers):
    if not numbers:
        return []
    first_parity = numbers[0]%2
    return[num for num in numbers if num % 2 == first_parity]