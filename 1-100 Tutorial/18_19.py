# i = int(input("Enter the number i:"))
# while(i>10 and i<100):
#     print(i)
#     i = i + 1
# print("Done with the loop")

# Break& Continue statement
# for i in range(20):
#     if(i==10):
#         break
#     print("5 *", i+1, "=", 5 * (i+1))
# print("Loop Drop")


for i in range(20):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 *", i, "=", 5 * (i+1))
print("Loop Drop")