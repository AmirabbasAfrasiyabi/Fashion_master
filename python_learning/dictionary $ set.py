"""
set
"""


# list_t = [1,2,3,4,5,5,2,1,4,7]
# set_t = set(list_t)
# print(set_t,list_t)

# set_t.add(11)
# print(set_t,list_t)


# set_1 = {1,2,3,4,5}
# set_2 = {4,5,6,7,8}

# #اجتماع
# print(set_1|set_2)

# #اشتراک
# print(set_1 & set_2)

# #difference
# print(set_1 - set_2)


"""
dict
"""

dict_t = {'key':'value' , 'name' : 'ali' , 'lastname':'amiri'}
dict_t['name'] = 'amirabbas'
# print(dict_t['name'])

# print(dict_t.get('name'))

#update
dict_t.update({'key':'hassan' , 'value' : 'amiri'})
# print(dict_t)

for k,v in dict_t.items():
    print(k,v)

for k in dict_t:
    print(dict_t[k])