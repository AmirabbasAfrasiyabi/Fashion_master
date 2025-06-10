"""
import random

def odd_and_evan_number(number):

    if number % 2 ==0:
        return "evan"
    else :
        return "odd"

random_number = random.randint(1,100)
result = odd_and_evan_number(random_number)
# print(f"the number of {random_number} is: {result}")


for i in range (5):
    test_random = random.randint(1,10)
    test_result = odd_and_evan_number(test_random)
    print(f"the number of {test_random} is: {test_result}")
"""




"""
def sum_function(n):
    sequence = list(range(0,n+1))
    print(sequence)

    total_sum = sum(sequence)
    return total_sum

user_input = int(input())
result = sum_function(user_input)
print(f"the sum of the integer within 0 to n+1 is {result}")
"""


"""
def separation_character(text):
    
    char_count=0
    number_count = 0

    for char in text:
        if char.isalpha():
            char_count +=1
        elif char.isdigit():
            number_count +=1
    
    return {"character":char_count , "numbers":number_count}

text_input = input()
result = separation_character(text_input)
print(result)
"""

