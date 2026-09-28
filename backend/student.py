class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks 

    def average(self):
        return sum(self.marks) / len(self.marks)