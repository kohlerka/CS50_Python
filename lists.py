students = ["Hermione", "Harry", "Ron"] # List of students


#Printing the names without a loop 
print(students[0]) # Hermione
print(students[1]) # Harry
print(students[2]) # Ronpy

#Printing the names with a loop. Here, without using a number
print("And now in a for-loop")

for student in students:
    print(student)

#Printing the names with a loop. Here, using a number
print("And now in a for-loop with a number")
for i in range(len(students)):
    print(i + 1, students[i])