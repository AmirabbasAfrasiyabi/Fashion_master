
class Human:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

    def fullname(self):
        return self.name +" "+self.lastname
    
    def __str__(self):
        return self.name + "___" +'object'

class Employee(Human):

    manager = 'amir'

    def programmer(self):
        print('I am a programmer')

    def full(self):
        return super().fullname()

p1 = Employee('ali','amiri')
p2 = Employee('hassan','amiri')

print(p1)
print(p1.name)
print(p1.fullname())
print(p1.manager)
p1.programmer()
print(p1.full())

print("_________________________")
print("_________________________")
print("_________________________")
print("_________________________")

print(p2)
print(p2.name)
print(p2.fullname())
print(p2.manager)
p2.programmer()
print(p2.full())

#magic method
# a = (2).__add__(3)
# print(a)