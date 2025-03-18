# a = input("Enter Your Name:")
# print("My name is ",a)
# x= input("Enter first number:")
# y= input("Enter first number:")
# print(x+y)
# print(int(x)+ int(y))


# Slicing with Skip value
# name ="Prakash"
# sl = name[0 : 2]
# print(sl)

# word = "amazing"
#sl = word[1:6:2]  
##string[start:end:step]
# sl = word[0:]
# sl = word[:7]
# print(sl)



# String Functions 
# x= len("Harry")
# print(x)

# name= "Harry"
# x = name.endswith("erry")
# print(x)

# name = "Prakash is a good boy"
# x = name.count("Prakash is a good boy")
# print(x)

# name = "prakash"
# x = name.capitalize() #This function capitalizes the first character of a given string
# print(x)

# name = "jfsdfhfsgfsdfuigfdjfg"
# x = name.find("gfs")
# print(x)

# name= "praaksh"
# x = name.replace("ak", "ka")
# print(x)



# Escape Sequence Characters
# print("My name is sidharth \\Verma")

# print("My Team:\nHackHounds\tLeader Sahab\'")


# str = "dskhJKHdKHhjujksfd hjkdf hjkdfkh  khd"
# print("str", str)
# print(str.strip,"\n")

# str = "dskhJKHdKHhjujksfd hjkdf hjkdfkh  khd!!!!!!!!!!!"
# print(str.rstrip("!"))
# for left side trailing characters, removes lstrip

# str = "Prakash a young boy do not want to use mobilephone for fun"
# print(str.split(" "))

# str = "Prakash a young boy do not want to use mobilephone for fun"
# print(str.center(100,"."))

# str = "Prakash a young boy do not want to use mobilephone for fun"
# print(str.endswith("for fun"))

# str = "Prakashayoungboydonotwanttousemobilephoneforfun"
# print(str.isalnum()) #using for In your case, the string "Prakash a young boy do not want to use mobile phone for fun" contains spaces, so isalnum() will return False.
# print(str.isalpha())

str = "Prakash Choudhary"
print(str.isprintable())
'''printable. Printable characters include letters, digits, punctuation, and whitespace (like spaces). Non-printable characters include things like control characters (e.g., \n for newline, \t for tab).'''


'''Lists and Tuples'''

# friends = ["Apple", "Akash", "Rohan", 18, 5, 2006, False, True]
'''Uses this is because in 
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
'''
# prefix = "Friend_"
# friends_with_prefix = [prefix + str(friend) if isinstance(friend, str) else friend for friend in friends]
# print(friends_with_prefix)

# list1= [7, 9, "Harry"]
# print(list1[0])
# print(list1[0:])


# List Methods
# list1= [1, 8, 7, 2, 21, 15]
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
# list1.append(8)
# print(list1)
# list1.insert(3, 8)
# print(list1)
# list1.pop(3)
# list1.pop(2)
# print(list1)
# list1.remove(21)
# print(list1)
