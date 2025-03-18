# for i in range(5):
#     print(i)
#     if i == 4:
#         break

# else: 
#     print("Sorry no i")

# i = 0
# while i <8:
#     print(i)
#     i = i + 1
#     if i == 4:
#         break

# else: 
#     print("Sorry no i")
    
# a = input("Enter the number: ")
# print( f"Multification table of {a} is:")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# # except Exception as e:
# except:
#     print("Invalid Input!")

# print("Some imp lines of code")
# print("End of Programme")

# try:
#     num = int(input("Enter an integer: "))
#     a = [ 6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer")
# except IndexError:
#     print("Index Error")


# # Finally keyword uses 
# def func1():
#     try:
#         l = [1, 5, 6, 7, 8]
#         i = int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some Error Occurred")
#         return 0
#     finally:
#         print("I am always executed")

# x = func1()
# print(x)



'''Raising custom errors in python'''
a = int(input("Enter any value  between 5 and 9"))

if(a <5 or a >9):
    raise ValueError("Value Error!, Should be betweeen 5 and 9")
