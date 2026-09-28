from .student import Student
from .operations import students


def save_students():
    with open("students.txt", "w") as file:
        for student in students.values():
            file.write(
                f"{student.roll_no}|{student.name}|{','.join(map(str, student.marks))}\n"
            )


def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll_no, name, marks_str = line.strip().split("|")

                roll_no = int(roll_no)
                marks = list(map(int, marks_str.split(",")))

                student = Student(roll_no, name, marks)
                students[roll_no] = student

    except FileNotFoundError:
        print("No existing student data found.")