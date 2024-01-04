class Student:
    count = 0 
    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))
        self.department = input("Enter the department (PGDM/B.Tech): ").capitalize() 
        Student.count += 1

    def display(self):
        print("Name: ", self.name, "Age: ", self.age, "Department:", self.department)
# Welcome message
print(""" 
STUDENT ADMIT
------------------""")
pgdm_students = []
btech_students = []
while True:
    new_student = Student()
    new_student.display()
    if new_student.department == 'P':
        pgdm_students.append(new_student)
    elif new_student.department == 'B':
        btech_students.append(new_student)
    user_input = input("Do you want to enter another student? (yes/no): ").lower()
    if user_input != 'yes':
        break 
print("\nPGDM Department Students:")
for student in pgdm_students:
    student.display()
print("\nB.Tech Department Students:")
for student in btech_students:
    student.display()
print("\nTotal number of students:", Student.count)