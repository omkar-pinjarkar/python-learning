'''
# a = "Om" # <class 'str'>
a = 10 # <class 'int'>

t = type(a)

print(t)
'''

# Example 1: Basic usage
a = 10
print(type(a))        # <class 'int'>

# Example 2: Different data types
print(type("Hello"))  # <class 'str'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>
print(type([1, 2]))   # <class 'list'>
print(type((1, 2)))   # <class 'tuple'>
print(type({"a": 1})) # <class 'dict'>

