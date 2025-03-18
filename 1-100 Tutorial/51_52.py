# with open ('myfile.txt', 'w') as f:
#     f.write('Hello World!')
#     f.truncate(5)
# # sekking for specific position

# with open('myfile.txt','r') as f:
#     print(f.read())

# with open('myfile2.txt', 'r') as f:
#   # Move to the 10th byte in the file
#   f.seek(10)

#   # Read the next 5 bytes
#   data = f.read(6)
#   print(data)

# tell() function
# with open('myfile2.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)

#   # Save the current position
#   current_position = f.tell()
#   print(current_position)

#   # Seek to the saved position
#   f.seek(current_position)
#   print(current_position)




# Lambda Function
# Function to double the input
# def double(x):
#   return x * 2

# Lambda function to double the input
# lam = lambda x: x * 2


# print(lam(6))

# Function to calculate the product of two numbers
# def multiply(x, y):
#     return x * y

# Lambda function to calculate the product of two numbers
# lam1 = lambda x, y: x * y
# print(lam1(2,3))


# Lambda function to calculate the product of two numbers,
# with additional print statement
# lam2 = lambda x, y: print(f'{x} * {y} = {x * y}')
# print(lam2(2, 3))


# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))