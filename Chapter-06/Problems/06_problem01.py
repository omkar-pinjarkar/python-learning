"""
Practice Set
1. Write a program to find the greatest of four numbers entered by the user.
CHAPTER 06
2. Write a program to find out whether a student has passed or failed if it requires a total of
40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
input from the user.
3. A spam comment is defined as a text containing following keywords: “Make a lot of
money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
4. Write a program to find whether a given username contains less than 10 characters or not.
5. Write a program which finds out whether a given name is present in a list or not.
scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 => C
50 – 60 => D
<50 => F
6. Write a program to calculate the grade of a student from his marks from the following
7. Write a program to find out whether a given post is talking about “Harry” or not
"""

a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print("Greatest number is a1:", a1)

elif(a2 > a1 and a2 > a3 and a2 > a4):
    print("Greatest number is a2:", a2)

elif(a3 > a1 and a3 > a2 and a3 > a4):
    print("Greatest number is a3:", a3)

elif(a4 > a1 and a4 > a2 and a4 > a3):
    print("Greatest number is a4:", a4)

else:
    print("None is greatest (some numbers are equal)")
