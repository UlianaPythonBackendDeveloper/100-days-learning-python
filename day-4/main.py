# How print on screen
print(5 <= 5)

# def is_pensioner
def is_pensioner(age: int) -> bool:
    return age >= 60

print(is_pensioner(age=70))

# 
print(len(' 1 '))
print('abc' > 'cba')
#print('abc' >= 3)

# is_long_word
def is_long_word(word):
    return len(word) > 5 

print(is_long_word(word='banana'))

#
print(10 % 2 ==0)
# def is_international_phone
def is_international_phone(number: str) -> bool:
    return number.startswith('+')

print(is_international_phone(number='+79774044589'))
print(is_international_phone(number='89999074589'))


print(12 > 40) or (400 >= 400)


# is_leap_year
def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(is_leap_year(year=2010))

# is_palindrome is_not_palindrome
def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]

def is_not_palindrome(word):
        return not is_palindrome(word)
    
    
print(False or 'yes')
print(True and False or True)

# def string_or_not 
def string_or_not(value):
    return 'yes' if isinstance(value,str) else 'no'

# guess_number
def guess_number(number):
    return 'You win!' if number == 45 else 'Try again!'

print(guess_number(number=25))