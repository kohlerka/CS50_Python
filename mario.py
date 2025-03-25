def main():
    print_column(3)
    print_row(4)
    print_square(5)
    print_square_easy(6)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width) #instead of using a loop, we can use the * operator to repeat the string

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()#print a newline after each row

def print_square_easy(size):
    for _ in range(size):
        print("x" * size)

main()