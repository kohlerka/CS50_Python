def main():
    number = get_number()
    miau(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n
        
def miau(n):
    for _ in range(n):
        print("miau")

main()