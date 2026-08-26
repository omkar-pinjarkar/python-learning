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
p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"

username = input("Enter username: ")

if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("Your username contains more than or equal to 10 characters")