"""

Practice Set
1. Write a program to print multiplication table of a given number using for loop.
CHAPTER 07
2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
3. Attempt problem 1 using while loop.
4. Write a program to find whether a given number is prime or not.
5. Write a program to find the sum of first n natural numbers using while loop.
6. Write a program to calculate the factorial of a given number using for loop.
7. Write a program to print the following star pattern.
*
***
***** for n = 3
8. Write a program to print the following star pattern:
*
**
*** for n = 3
* * for n = 3
* * *
9. Write a program to print the following star pattern.
* * *
10. Write a program to print multiplication table of n using for loops in reversed order.
"""

l = ["Harry","Soham","Sachin","Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")