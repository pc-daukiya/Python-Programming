# Inheritance
'''Types of inheritance:
Single inheritance
Multiple inheritance
Multilevel inheritance
Hierarchical Inheritance
Hybrid Inheritance'''

'''Single Inheritance:
Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.'''

'''Multiple Inheritance:
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.'''

'''Multilevel Inheritance :
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.'''

'''Hierarchical Inheritance:
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.'''

'''Hybrid Inheritance:
Inheritance consisting of multiple types of inheritance is called hybrid inheritance.'''

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def showdetails(self):
#         print(f"The name of Employee: {self.id} is {self.name}")

# class Programmer(Employee):
#     def showLang(self):
#         print("The Python Language is default")

# e1 = Employee("RohanDas", 401)
# e1.showdetails()
# e2 = Programmer("Prakash", 105)
# e2.showdetails()
# e2.showLang()


# # e1.showLang()  #This is show error because a grandfather don't take directly action to father'son
 
 
 
'''
Types of access specifiers
Public access modifier
Private access modifier
Protected access modifier

'''

# For Checking Private Class/ This is example of private class uses 
# class MyClass:
#     def __init__(self):
#         self._nonmangled_attribute = "I am a nonmangled attribute"
#         self.__mangled_attribute = "I am a mangled attribute"

# my_object = MyClass()

# print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
# print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute


class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())