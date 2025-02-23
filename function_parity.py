def main():
    x = int(input("What is x? "))
    if is_even(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")   

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    #you could do the same by writing: return True if n % 2 == 0 else False
    # or even shorter: return n % 2 == 0 --> as this is already a boolean expression
main()