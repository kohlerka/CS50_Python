# a float is a number with a floating decimal point
x = float(input("What is x: "))
y = float(input("What is y: "))
print(f"{x} + {y} = {x + y}")

# Custom function for Swiss formatting
def swiss_format(number):
    formatted_number = f"{number:,.2f}"
    swiss_formatted_number = formatted_number.replace(",", "'")
    return swiss_formatted_number

# Example usage
a = float(input("Enter a number: "))
print(a)
print("round()", round(a))
print("round(1)", round(a, 1))
print(f"{a: ,}")

# Formatting numbers
print(f"{a}")
print(f"{a: ,}")  # American formatting
print(f"{a: .2f}")  # 2 decimal places
print(swiss_format(a))  # Swiss formatting