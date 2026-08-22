"""Practice Set
1. Write a program to print Twinkle twinkle little star poem in python.
2. Use REPL and print the table of 5 using it.
3. Install an external module and use it to perform an operation of your interest.
online for the function which does that.
CHAPTER 01
4. Write a python program to print the contents of a directory using the os module. Search
5. Label the program written in problem 4 with comments 
"""

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text - hello Tony")
engine.runAndWait()