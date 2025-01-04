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

# Title case
print("Enter a string for using title case")
title = input()
title = title.title()
print("You entered:", title)

# Do all at the same time
print("Enter a string for using all at the same time")
all = input()
all = all.strip().title()
print("Removing space and title case:", all)


# Splitting a string
print("Enter your full name")
vorname, nachname = input().split()
print("Vorname:", vorname)
print("Nachname:", nachname)
