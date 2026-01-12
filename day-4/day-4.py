# def normalize_url
def normalize_url(address):
    if address.startswith('https://'):
        return address
    elif address.startswith('http://'):
        return 'https://' + address[7:]
    else:
        return 'https://' + address
    
print(normalize_url('google.com'))
#
def calculate_weather(temperature):
    if temperature > 20:
        print("Too warm")
    elif temperature < 20:
        return "Too cold"
    
print(calculate_weather(22))

# def who_is_this_home_to_starks
def who_is_this_house_to_starks(house_name):
    if house_name in('Karstark', 'Tully'):
        return 'friend'
    elif house_name in ('Lannister','Frey'):
        return 'enemy'
    else:
        return 'neutral'
    
print(who_is_this_house_to_starks('Frey'))
# 
def abs(number:int) -> int:
    return number if number >= 0 else -number

print(abs(5))

# 
def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hello.'))

num = 6
result  = num + 1 if num % 2 != 0 else 1 - num
print(result)
# flip_flop
def flip_flop(text):
    return 'flop' if text == 'flip' else 'flip'

print(flip_flop('flop'))

def count_items(count):
    match count:
        case 1:
            return 'one'
        case 2:
            return 'two'
        case _:
            return None

print(count_items(count=1))
            
def get_number_explanation(number):
    if number == 666:
        return 'devil number'
    elif number == 42:
        return 'answer for everything'
    elif number == 7:
        return 'prime number'
    else:
        return 'just a number'
    
print(get_number_explanation(666))
print(get_number_explanation(8))
print(get_number_explanation(42))
print(get_number_explanation(7))

def print_numbers(n: int) -> None:
    i = 1 
    while i <= n:
        print(i)
        i = i + 1
        print("Finished")
        
print_numbers(3)

a = 0
while a < 3:
    print(a)
    a += 1
    
def greet():
    count = 0
    while True:
        print('Hello')
        count += 1
greet()

