# Object Oriented Programming 
# class --> Object --> Inheritance -->Encapsulation --> Polymorphism

# class Person:
#     name = "Prakash"
#     occupation = "Software Developer"
#     networth = 10
    
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
# a = Person()
# a.name = "Harry"
# a.networth = 500
# print(a.name, a.occupation, a.networth)
# a.info()

# Constructor in Python
class Person:
    
  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
# c = Person(1,2,3) #There is given error because there is we take 3 values and one is self c taken value then this will be happen 4 values So nOw edited is 
c = Person(1,2)
a.info()
b.info()
# c.info()