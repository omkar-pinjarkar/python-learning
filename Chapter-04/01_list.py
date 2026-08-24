# list is mutable 

friend = ["Apple","Orange",345.06,"Rohan",False,"Akash",5]

print(friend[0])  # Apple
print(friend[1])  # Orange

# First change the value, then print it
friend[3] = "Grapes"
print(friend[3])  # Grapes   
print(friend[1:4])
