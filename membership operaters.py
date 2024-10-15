students = {
    "spongebob": "A",
    "squidward": "B",
    "patrick": "C"
}

student = input("Enter the name of the student: ")
if student in students:
    print(f"{student} was found with grade {students[student]}")
else:
    print(f"{student} was not found")

print("Thanks for using the platform!")
