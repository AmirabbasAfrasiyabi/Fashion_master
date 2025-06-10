class Employee :
    salary = 3000
    
    def __init__(self,first_name,Last_name):
        self.first_name = first_name
        self.last_name = Last_name

    def get_full_name(self):
        return self.first_name + "  " + self.last_name
    
    def get_salary(self):
        return self.salary
    
Employee_1 = Employee('Ali','Amiri')
Employee_2 = Employee('Amir' , 'Afrasiabi')

print(Employee_1.get_full_name())
print(Employee_2.get_full_name())

print(Employee_1.get_salary())
print(Employee_2.get_salary())