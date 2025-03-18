# age = int(input("Enter your age in whole number:"))
# if (age >=18 and age<=70):
#     print("You are adult and you can drive")
# elif (age <18 and age >=13):
#     print("You are teenager")
# elif (age<13 and age>=1):
#     print("You are child")
# else:
#     print("Seriously You alive or you can message")
    
# Exercise 
import time
timestamp = time.strftime ('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
min=int(time.strftime('%M'))

if(hour>=5 and hour<=11 and min>=0 and min<=59):
  print("Good Morning Sir")

if(hour>=12 and hour<=17 and min>=0 and min<=59):
  print("Good Afternoon Sir")

if(hour>=18 and hour<=23 and hour>=0 and hour<=4 and min>=0 and min<=59):
  print("Good Evening Sir")
