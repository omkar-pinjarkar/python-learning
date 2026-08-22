"""Practice Set
1. Write a program to print Twinkle twinkle little star poem in python.
2. Use REPL and print the table of 5 using it.
3. Install an external module and use it to perform an operation of your interest.
online for the function which does that.
CHAPTER 01
4. Write a python program to print the contents of a directory using the os module. Search
5. Label the program written in problem 4 with comments 
"""

print("------------------------------------------------------")


print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.""")

print("------------------------------------------------------")


# Use raw string (r prefix) to avoid unicode escape issues
"""
PS C:\\Users\\Omkar pinjarkar> python
Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5*1
5
>>> 5*2
10
>>> 5*3
15
>>> 5*4
20
>>> 5*5
25
>>> 5*6
30
>>> 5*7
35
>>> 5*8
40
>>> 5*9
45
>>> 5*10
50
>>>
"""
print("------------------------------------------------------")

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text - hello Tony")
engine.runAndWait()



import os

# Specify the directory whose contents we want to display
path = r"C:\Users\Omkar pinjarkar\Desktop"

# Get all files and directories inside the specified path
contents = os.listdir(path)

# Print each item on a separate line
print(*contents, sep="\n")