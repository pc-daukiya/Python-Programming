'''Exercise 11 - Drink Water Reminder
Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system'''

# Exercise Soluction
import time
import ctypes
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the computer speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to display a message box
def show_alert(message, title="Reminder"):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)

# Interval in seconds (1 hour = 3600 seconds)
REPEAT_INTERVAL = 10

while True:
    speak("Hey Prakash, drink water")
    show_alert("Hey Prakash, Drink water")
    time.sleep(REPEAT_INTERVAL)
