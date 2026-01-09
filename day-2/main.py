# use method min
print(min(3,10,22,-3,0))
#  Nothing determinirv
# from random import random

# print(random() * 10)
# task
from random import random
print(round(random()*10))
# object
company = "hexlet"
print(company.capitalize())
# task lowercase text
text = "a MIND needs Books as a Sword needS a WHETSTONE."

# BEGIN (write your solution here)
print(text.lower())
# END
# 
company = "Hexlet"
print(company.lower())
# task strip()
first_name = '  Grigor   \n '

# BEGIN (write your solution here)
first_name = '  Grigor   \n '.strip()
print(first_name)
# END
# slice
text = 'hexlet'
length = text.upper().count('E')
print(length)
# 
company = "Hexlet"
print(company.upper().lower().upper().lower().upper().lower())