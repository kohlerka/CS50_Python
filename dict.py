students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

print("And now in a for-loop")
for student in students:
    print(student) # This will print the keys

print("And now in a for-loop showing key and value")
for student in students:
    print(student, students[student]) # This will print the key and value

print("And now changing the default separator")
for student in students:
    print(student, students[student], sep=" is in ") # It could also be e.g a comma instead of " is in "

# I now do a list of dictionaries with three key-value pairs
# The keys are "name", "house" and "patronus"
students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter",
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag",
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell Terrier",
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": "None", # if there is no value for a key, you can write None
    },
]   

for student in students:
    print(student["name"], student["house"], student["patronus"])
