# This file is to test what David from CS50 tells about strings in python
# https://docs.python.org/3/library/stdtypes.html#string-methods
print("Enter extra spaces")
s = input()
print("You entered:", s)
s = s.strip() # s is a string. strip() is a method of the string class
print("You entered:", s)

# Capitalize the first letter of the string
print("Enter a string")
cap = input()   # cap is a string
cap = cap.capitalize()
print("You entered:", cap)