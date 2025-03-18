# x = 10 

# def my_function():
#   global x
#   x = 5 
#   y = 5 
#   print("Y is:")
#   print(y)

# my_function()
# print("X is:")
# print(x)



# File IO
# READING A FILE
# f = open('myfile.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE
# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()

# with open('myfile.txt', 'a') as f:
#   f.write("Hey I am inside with")


# read(), readlines() and writelines()

# f = open('myfile.txt', 'r')
# i =0
# while True:
#     i = i +1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of Student {i} in Maths is:{m1*2}")
#     print(f"Marks of Student {i} in Maths is:{m2*2}")
#     print(f"Marks of Student {i} in Maths is:{m3*2}")
    
#     print(line)

# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()
    