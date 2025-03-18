'''Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class'''

'''Code 1'''
# class Math:
#     def __init__(self, num):
#         self.num = num

#     def addtonum(self, n):
#         self.num = self.num +n
    
#     @staticmethod
#     def add(a, b):
#       return a + b

# # result = Math.add(1, 2)
# # print(result) # Output: 3
# a = Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

# print(Math.add(7, 2))

'''Instance Varible vs class Variable'''
'''In summary, class variables are shared among all instances of a class and are used to store information that is common to all instances. Instance variables are unique to each instance of a class and are used to store information that is specific to each instance. Understanding the difference between class variables and instance variables is crucial for writing efficient and maintainable code in Python.'''
'''Code 2'''
# class Employee:
#     def __init__(self, name):
#         self.name = name
        
#     def showDetails(self):
#         print(f"The name of the employee is {self.name}")

# emp1 = Employee("Prakash")
# emp1.showDetails()
# emp2 = Employee("Rohan")
# emp2.showDetails()
# emp3 = Employee("Raghav")
# Employee.showDetails(emp3)


'''Code 3'''
# class Employee:
#     companyName = "Apple"
#     noOfEmployees = 0
#     def __init__(self, name):
#         self.name = name
#         self.raise_amount = 0.02
#         Employee.noOfEmployees +=1
#     def showDetails(self):
#         print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# # Employee.showDetails(emp1)
# emp1 = Employee("Harry")
# emp1.raise_amount = 0.3
# emp1.companyName = "Apple India" 
# emp1.showDetails()
# Employee.companyName = "Google"
# print(Employee.companyName)

# emp2 = Employee("Rohan")
# emp2.companyName = "Nestle"
# emp2.showDetails()



