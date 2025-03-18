# Short hand If else Statements
# a = 3300
# b = 1233
# print("A") if a>b else print("=") if a==b else print("B")

# c = 10 if a>b else 0
# print(c)

# enumerate function in python
marks = [12, 56, 65, 99, 12, 1, 33, 4]
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(mark==99):
        continue
    
    if(index==3 ):
        print( f"Awensome Marks!\n{marks[3]}")
        
#  In 43 video's something related to vitual environment in python
# How to import process
# python -m venv myenv  