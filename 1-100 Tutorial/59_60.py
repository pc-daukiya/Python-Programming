# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx
    
# @greet
# def hello():
#     print("Hello World!")

# @greet
# def add(a, b):
#     print(a+b)


# hello()
# # greet(add)(1, 2)
# add(1, 2)



# Getters and Setters
# class MyClass:
#     def __init__(self, value):
#         self._value = value
    
#     def show(self):
#         print(f"Value is {self._value}")
    
#     @property #getters uses aas @property
    
#     def ten_value(self):
#         return 10* self._value
    
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10

# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()
