
"""
def decorator(func):

    def wrapper():
        print('before')
        result = func()
        print('after')
        return result

    return wrapper

@decorator
def hello():
    print('hello')

hello()
"""




#timing
"""
import time

def timer(func):
    def wrapper():

        start = time.time()
        func()
        end = time.time() - start
        print(f'took {end} second to execute')

    return wrapper

@timer
def counter():

    total = 0
    for char in range(1,100000):
        total += char

    return total

counter()
"""


