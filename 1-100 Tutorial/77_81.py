'''Operator Overloading'''
# How to overload an operator in Python?
'''+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__'''


'''Code 1'''
# class Vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self, x):
#         return Vector(self.i + x.i, self.j + x.j, self.k+x.k)
# v1 = Vector(1, 2 , 3)
# print(v1)

# v2 = Vector(5, 6 , 8)
# print(v2)

# print(v1 + v2)
# print(type(v1 + v2))

'''Code 2'''  #Single Inheritance
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")

# d = Dog("Dog", "Doggerman")
# d.make_sound()

# a = Animal("Dog", "Dog")
# a.make_sound()

# '''Code 3'''
# class Employee:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(f"The name is {self.name}")
        
# class Dancer:
#     def __init__(self, dance):
#         self.dance = dance
#     def show(self):
#         print(f"The dance is {self.dance}")
        
# class DancerEmployee(Employee, Dancer):
#     def __init__(self, dance, name):
#         self.dance = dance
#         self.name = name
        
# o = DancerEmployee("Kathak", "Shivani")
# print(o.name)
# o.show()
# print(o.dance)
# o.show()
'''Operator Overloading'''
# How to overload an operator in Python?
'''+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__'''


'''Code 1'''
# class Vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self, x):
#         return Vector(self.i + x.i, self.j + x.j, self.k+x.k)
# v1 = Vector(1, 2 , 3)
# print(v1)

# v2 = Vector(5, 6 , 8)
# print(v2)

# print(v1 + v2)
# print(type(v1 + v2))

'''Code 2'''  # Single Inheritance
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")

# d = Dog("Dog", "Doggerman")
# d.make_sound()

# a = Animal("Dog", "Dog")
# a.make_sound()

'''Code 3'''  # Multiple Inheritance
# class Employee:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(f"The name is {self.name}")
        
# class Dancer:
#     def __init__(self, dance):
#         self.dance = dance
#     def show(self):
#         print(f"The dance is {self.dance}")
        
# class DancerEmployee(Employee, Dancer): 
#     def __init__(self, dance, name):
#         self.dance = dance
#         self.name = name
        
# o = DancerEmployee("Kathak", "Shivani")
# print(o.name)
# print(o.dance)
# o.show()
# print(DancerEmployee.mro())

'''Code 4''' # Multilevel Inheritance
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o = Dog("tommy", "Black")
# o.show_details()
# print(GoldenRetriever.mro())


'''Code 5''' # Example of Hybrid Inheritance 
# class BaseClass:
#   pass

# class Derived1(BaseClass):
#   pass  

# class Derived2(BaseClass):
#   pass  

# class Derived3(Derived1, Derived2):
#   pass

                                # Hierarchical Inheritance
# class BaseClass:
#   pass

# class D1(BaseClass):
#   pass

# class D2(BaseClass):
#   pass

# class D3(D1):
#   pass