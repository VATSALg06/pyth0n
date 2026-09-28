from .student import Student

students = {}


def add_student(roll_no, name, marks):
    student = Student(roll_no, name, marks)
    students[roll_no] = student

    return student


def get_student(roll_no):
    if roll_no in students:
        return students[roll_no]

    return None


def get_all_students():
    return students.values()


def update_student(roll_no, name=None, marks=None):
    if roll_no not in students:
        return False

    student = students[roll_no]

    if name:
        student.name = name

    if marks:
        student.marks = marks

    return True


def delete_student(roll_no):
    if roll_no not in students:
        return False

    del students[roll_no]

    return True