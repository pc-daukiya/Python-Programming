'''Exercise 4'''
# Simple make a code in which name is converts in Decoding language and this is understandable for me my decoder Make This exercise


name = input("Enter Your Message:")
reversed_name = name[:: -1]

first_char = name[0]
remaining_name = name[1:]
modified_name = "ght" + remaining_name + first_char + "cve"
# upadate_name = name
x = len(name)
if (x <= 3):
    print("Decoding message is: ", reversed_name)
    
if ( x>3):
    print("Decoding message is: ", modified_name)