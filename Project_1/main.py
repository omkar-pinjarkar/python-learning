"""Project 1 : Snake Water Gun Game
Project
We all have played snake, water gun game in our childhood. If you havenʼt,
google the rules of this game and write a python program capable of playing
this game with the user
"""

"""
1 for Snake
-1 for water
0 for gun

"""
import random

'''
1 for snake
-1 for water 
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Validate input
if youstr not in youDict:
    print("Invalid choice! Please enter s, w, or g.")
    exit()

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("Its a draw")

else:
    # Logic: 
    # You win when: (computer - you) == -2 (computer:water, you:snake) 
    #              or (computer - you) == 1 (computer:gun, you:water or computer:snake, you:gun)
    # You lose when: (computer - you) == -1 (computer:water, you:gun or computer:gun, you:snake)
    #                or (computer - you) == 2 (computer:snake, you:water)
    
    if (computer - you) == -1 or (computer - you) == 2:
        print("You lose!")
    else:
        print("You win!")