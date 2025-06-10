
try:
    print('before')
    print(7/0)
    print('after')
except ZeroDivisionError:
    print("did not cause of a problem")

finally:
    print('end of the program')

