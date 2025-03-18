import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 50):
    os.mkdir(f"os_module_46/data/Day{i+1}")

