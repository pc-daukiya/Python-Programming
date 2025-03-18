# # Sets in Python
# s = {2, 4, 5, 6 ,7, 3, 2, 6}
# print(s)

# info = {"Calrls", 19, False,  True, 5.9, 19}
# print(info)

# # How to make a empty set
# Harry = {}
# print(type(Harry)) #This is wrong for display a empty set

# harry = set()
# print(type(harry)) #This is right way to display a empty set

# for value in info:
#     print(value)



# Set Methods
s1 = {1, 5, 3, 4}
s2 = {2,3,4, 5, 6, 7, 8, 8 , 9}
s3 = {21,31,14, 15, 16, 17, 18, 18 , 19}

print(s1.union(s2))
print(s1, s2)
print(s2.update(s1))
print(s1.intersection(s2))

sl = s1.symmetric_difference(s2)
sd = s1.symmetric_difference_update(s2)
print(sl)
print(sd)

print(s2.isdisjoint(s1))
print(s2.isdisjoint(s3))

print(s1.issuperset(s2))
print(s1.issubset(s2))


s3.remove(31)
print(s3)

# s3.remove(311)
# print(s3) # Give Key Error 

s3.discard(311)
print(s3) # Don't Key Error 

#del s1
# print(s1)

# s1.clear()
# print(s1)

item = s2.pop()
print(s2)
print(item)