class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks 

    def average(self):
       return  sum(self.marks) / len(self.marks) 

students = {}

def add_student():
    roll_no = int(input("Enter roll number: "))
    name = input("Enter student name:")
    marks = list(map(int, input("Enter 3 marks seperated by space:").split()))
    student = Student(roll_no, name, marks)
    students[roll_no] = student
    save_students()  # Save students to file after adding a new student
    print("Student added successfully!")



def view_student():
    roll_no = int(input("Enter roll number: "))
    if roll_no in students:
        student = students[roll_no]
        print(f"Roll Number: {student.roll_no}")
        print(f"Name: {student.name}")
        print(f"Marks: {student.marks}")
        print(f"Average: {student.average()}")
    else:
        print("Student not found!")

def view_all_students():
    if not students:
        print("No students found!")
        return

    for roll_no, student in students.items():
        print(f"Roll Number: {student.roll_no}")
        print(f"Name: {student.name}")
        print(f"Marks: {student.marks}")
        print(f"Average: {student.average()}")
        print("------------------------")

def update_student():
    roll_no= int(input("Enter the roll no."))
    if roll_no in students:
        student = students[roll_no]
        print(f"Current Name: {student.name}")
        new_name = input("Enter new name (leave blank to keep current): ")
        if new_name:
            student.name = new_name

        print(f"Current Marks: {student.marks}")
        new_marks_input = input("Enter new marks separated by space (leave blank to keep current): ")
        if new_marks_input:
            new_marks = list(map(int, new_marks_input.split()))
            student.marks = new_marks
        save_students()  # Save students to file after updating a student
        print("Student updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    roll_no = int(input("Enter the roll no.: "))

    if roll_no in students:
        del students[roll_no]
        save_students()  # Save students to file after deleting a student
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def save_students():
    with open("students.txt", "w") as file:
        for student in students.values():
            file.write(f"{student.roll_no}|{student.name}|{','.join(map(str, student.marks))}\n")


def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll_no, name, marks_str = line.strip().split("|")
                marks = list(map(int, marks_str.split(",")))
                roll_no = int(roll_no)
                student = Student(roll_no, name, marks)
                students[roll_no] = student
    except FileNotFoundError:
        print("No existing student data found.")



load_students()  # Load students from file when the program starts

while True:
    print("Welcome to the Student Management System")
    print ("-------------------------------")
    print("MENU")
    print("1. Add Student")
    print("2. View Student")    
    print("3. View All Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("-------------------------------")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        view_all_students()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice!")  



