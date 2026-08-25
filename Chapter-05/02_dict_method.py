marks = {
    "Harry": 100,
    "Shubham":56,
    "Rohan" : 23,
    0: "Harry"
}
#print(marks.items())
#print(marks.keys())
#marks.update({"Harry":99,"Renuka":100})
#print(marks)


print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error