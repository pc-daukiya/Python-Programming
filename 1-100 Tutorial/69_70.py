# Python Class Methods
'''It's important to note that class methods cannot modify the class in any way. If you need to modify the class, you should use a class level variable instead.'''

'''Code 1'''
# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany
        

# e1 = Employee()
# e1.name = "Prakash"
# e1.show()
# # print(Employee.company)
# e1.changeCompany("Tesla")
# e1.show()
# # print(Employee.company)


# Class methods as alternative constructors
'''Code 2'''
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     @classmethod
#     def fromStr(cls, String):
#         return cls(String.split("-")[0], int(String.split("-")[1]))

# e1 = Employee("Prakash", 12000)
# print(e1.name)
# print(e1.salary)

# String = "John-12000"
# e2 = Employee.fromStr(String)
# print(e2.name)
# print(e2.salary)

# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     @classmethod
#     def from_String(cls, String):
#         name, age, gender= String.split(',')
#         return cls(name, int(age), gender)

# person = Person.from_String("Prakash Choudhary, 19, Male")
# print(person.name, person.age, person.gender)


