def print_reversed_numbers(number):
    current = number
    while current > 0:
        print(current)
        current -= 1
    print('finished!')

print_reversed_numbers(4)