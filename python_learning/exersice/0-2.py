"""
def correct_login():

    username = input()
    password = input()

    correct_username = "admin"
    correct_password = "admin"

    if username ==correct_username and password == correct_password:
        print('successful login')
    elif username == correct_username and password != correct_password:
        print('incorrect password')
    elif username != correct_username:
        print("user not found")


print("==login system==")
result = correct_login()
print (f"{result}")
"""


"""
List_1 = [1, 2, 3, 4, 5]
List_2 = [4, 12, 6, 7, 8]

print("list1:", List_1)
print("list2:", List_2)


merged_list = List_1 + List_2
print("final list:", merged_list)

unique_list = list(set(merged_list))
print("list to tuple is :", unique_list)

unique_list.sort()
print("list to tuple is :", unique_list)

first_three_number = unique_list[:3]
print(first_three_number)

"""