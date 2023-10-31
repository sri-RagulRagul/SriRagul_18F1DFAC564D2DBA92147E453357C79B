class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"{self.name}, Roll Number: {self.roll_number}, CGPA: {self.cgpa}"

def sort_students(student_list):
    return sorted(student_list, key=lambda x: x.cgpa, reverse=True)

# Test the function with different input lists of students
students_list = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.5),
    Student("Charlie", "C003", 3.9),
    Student("David", "D004", 3.7)
]

sorted_students = sort_students(students_list)
for student in sorted_students:
    print(student)
  