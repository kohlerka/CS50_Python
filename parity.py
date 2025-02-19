#How to use % modulo
# % is the modulo operator, which returns the remainder of dividing the left hand operand by right hand operand.
# For example, 9 % 4 would return 1 because 9 divided by 4 is 2 with a remainder of 1.
# The modulo operator is useful for finding out if a number is even or odd.
x = int(input("What is your number? "))
if x % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")