import os
folders = os.listdir("data")

# print(folders)
print(os.getcwd())
os.chdir("/Python")
print(os.getcwd())



# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

import os
folders = os.listdir("data")

print(folders)
# print(os.getcwd())
# os.chdir("/Python")
# print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

