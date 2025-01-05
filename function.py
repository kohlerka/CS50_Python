# This file is to test code from week 1, section def/functions

# Define the main function (calling it at the end of the file)
def main():
    # Ask for the users name and print it
    hello()
    name = input("What is your name? ")
    hello(name)

    # Do some calculations
    x = int(input("What is x: "))
    print("x squared is", square(x))

# in general this is the section with all the functions
# Define a function called hello

def hello(to="world"): # with the default value of "world"
    print("Hello", to)

def square(n):
    return n * n

main()  # Call the main function