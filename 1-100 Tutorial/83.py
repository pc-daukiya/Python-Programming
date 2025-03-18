# Exercise 9
'''Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

l = ["Rahul", "Nishant", "Harry"]
Your program should pronouce:

Shoutout to Rahul
Shoutout to Nishant
Shoutout to Harry
Note: If you are not using windows, try to figure out how to do the same thing using some other package'''

#Exercise Soluction
 
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

names = ["StupidProgramm1", "ItZgooseBoy", "Iswastikmishra", "srisridmulti", 
         "AvishJain24", "MFaizan3", "anukoolchauhan", "codeWithPrawar", 
         "ArshitRupani", "Muhammad-Anas11"]

for name in names:
    # Create the shoutout message
    shoutout_message = f'Shoutout to {name}'
    # Speak the message
    engine.say(shoutout_message)
    engine.runAndWait()
