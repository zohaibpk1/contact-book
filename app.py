student = {
    "name": "John Doe",
    "age": 20,
    "email": "john.doe@example.com",
    "roll_number": "A123",
    "courses": ["Math", "Science", "English"],
    "subject": "Physics"
}

print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")