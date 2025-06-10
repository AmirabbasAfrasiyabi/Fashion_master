# """
# list
# """
list = [1,2,3,4,"ali",[1,2,3]]

print(list)
print(type(list))
print(list[-1][2])
list[0] = 15
print(list)

list.append(123)
print(list)

list.insert(1,"hello")
print(list)

print(len(list))
print("hello" in list)

"""
slicing
"""
print(list[0:5])
print(list[2:])
print(list[:5])


"""
tuple
"""
tuple = tuple(list)
print(tuple)
print(type((1)))
print(type((1,)))