from collections import namedtuple

# Define the named tuple structure
Student = namedtuple('Student', ['name', 'age', 'department'])

# List of student data
student_data = [
    ("Alina", "22", "linguistics"),
    ("Alex", "25", "programming"),
    ("Kate", "19", "art")
]

# Create named tuple instances and print them
for data in student_data:
    student = Student(*data)
    print(student)