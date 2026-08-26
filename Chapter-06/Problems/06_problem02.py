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

# Take marks as input from user
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))

# Calculate total marks and percentage
total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100

# Check conditions for passing
if(sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and percentage >= 40):
    print(f"Congratulations! You have PASSED!")
    print(f"Total Marks: {total_marks}/300")
    print(f"Percentage: {percentage:.2f}%")
else:
    print(f"Sorry! You have FAILED.")
    print(f"Total Marks: {total_marks}/300")
    print(f"Percentage: {percentage:.2f}%")
    
    # Show which subject(s) the student failed in
    if(sub1 < 33):
        print(f"Failed in Subject 1: {sub1}/100 (Need at least 33)")
    if(sub2 < 33):
        print(f"Failed in Subject 2: {sub2}/100 (Need at least 33)")
    if(sub3 < 33):
        print(f"Failed in Subject 3: {sub3}/100 (Need at least 33)")
    if(percentage < 40):
        print(f"Overall percentage is below 40%")