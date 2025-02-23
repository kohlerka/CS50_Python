i = 3
while i != 0:   # != means not equal to
    print("Miau")
    i -= 1 #easier way to write i = i - 1

#you can do it also the other way around
i = 0
while i < 3:
    print("Wau")
    i += 1 #easier way to write i = i + 1

# The code below will is an example of how to do exception handling
# The code will keep asking for a number until a positive number is entered
while True:
    n = int(input("Enter a number: "))
    if n > 0:
        break
for _ in range(n):
    print("Hello")