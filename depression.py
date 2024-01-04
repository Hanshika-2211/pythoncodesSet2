class Student:
    count = 0
    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))
        self.department = input("Enter the department (PGDM(p)/B.Tech(b)): ").capitalize()
        Student.count += 1
    def display(self):
        print("Name:", self.name, "Age:", self.age, "Department:", self.department)
print("""
STUDENT ADMIT
------------------""")
pgdm_students = []
btech_students = []
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    new_student = Student()
    new_student.display()
    if new_student.department == 'P':
        pgdm_students.append(new_student)
    elif new_student.department == 'B':
        btech_students.append(new_student)
print("*******")
print("\nPGDM Department Students:")
for student in pgdm_students:
    student.display()
print("\nB.Tech Department Students:")
for student in btech_students:
    student.display()
print("\nTotal number of students:", Student.count)