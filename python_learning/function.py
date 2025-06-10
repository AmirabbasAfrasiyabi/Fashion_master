# def print_hello():
#     for i in range(3):
#         print('hello')

# print_hello()
# print(print_hello())


# def aca():
#     print('done')

# def cs():
#     return 3

# print(aca())
# print(cs())

"""
args and kwargs
"""
# def test(*args):
#     print(type(args))

# test(1,2,3,4,5,6)

# def test(**kwargs):
#     print(kwargs)

# test(name='ali',lastname='amiri')


"""
delta
"""

def delta(a,b,c):
    return ((b**2)-(4*a*c))

print(delta(3,4,5))