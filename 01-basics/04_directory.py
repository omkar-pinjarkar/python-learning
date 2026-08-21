"""Practice Set
1. Write a program to print Twinkle twinkle little star poem in python.
2. Use REPL and print the table of 5 using it.
3. Install an external module and use it to perform an operation of your interest.
online for the function which does that.
CHAPTER 01
4. Write a python program to print the contents of a directory using the os module. Search
5. Label the program written in problem 4 with comments 
"""

import os

# Specify the directory whose contents we want to display
path = r"C:\Users\Omkar pinjarkar\Desktop"

# Get all files and directories inside the specified path
contents = os.listdir(path)

# Print each item on a separate line
print(*contents, sep="\n")