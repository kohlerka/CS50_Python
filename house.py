name = input("What is your name? ")

if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")
elif name == "Ron":
    print("Griffindor")
# We could also do if name == "Harry" or name == "Hermione" or name == "Ron":
# but that's a lot of repetition. We can use the in operator to check if a value is in a list.
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#solution with match and case
name = input("What is your name? ")

match name:
    case "Harry"| "Hermione" |"Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
   