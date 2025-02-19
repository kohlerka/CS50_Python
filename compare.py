x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

#There is also another way of doing it
print("Version with or")
if x < y or x > y:
    print("x is not equal to y") 
else:    
    print("x is equal to y")       

#And now you can ask if it's not equal to y
print("version with not equal")
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Just to show the "and" operator
print("Version with and")
   
