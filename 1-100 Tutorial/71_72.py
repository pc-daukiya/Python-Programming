# class Person:
#       def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       self.version = 1

    
# p = Person("John", 30)
# print(p.__dict__)

# print(help(Person))


'''Super Keyword'''
# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

# class Programmer(Employee):
#     def __init__(self, name, id, lang):
#         # super().__init__( name, id)
#         self.lang = lang

# rohan = Employee("Rohan Das", "420")
# harry = Programmer("Harry", "2345", "Python")
# print(rohan.name)
# print(rohan.id)
# print(harry.lang)

# Code3
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__( name, id)
        self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(rohan.id)
print(rohan.name)
print(harry.id)
print(harry.name)
print(harry.lang)