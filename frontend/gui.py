import tkinter as tk
from tkinter import messagebox
from backend.storage import save_students
from backend.operations import (
        add_student, 
        get_student,
        get_all_students,
        update_student,
        delete_student
)

def start_gui():

    window = tk.Tk()
    window.title("Student Management System")
    window.geometry("500x400")

    def add_student_ui():
        add_window = tk.Toplevel(window)
        add_window.title("Add Student")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Roll Number").pack()
        roll_entry = tk.Entry(add_window)
        roll_entry.pack()

        tk.Label(add_window, text="Name").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Marks").pack()
        marks_entry = tk.Entry(add_window)
        marks_entry.pack()

        def submit_student():
            try:
                roll_no = int(roll_entry.get())
                name = name_entry.get()
                marks = list(map(int, marks_entry.get().split()))

                add_student(roll_no, name, marks)
                save_students()

                messagebox.showinfo(
                    "Success",
                    "Student added successfully!"
                )

                add_window.destroy()

            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter valid numbers for roll number and marks."
                )

        tk.Button(
            add_window,
            text="Add Student",
            command=submit_student
        ).pack(pady=20)


    def view_student_ui():
        view_window = tk.Toplevel(window)
        view_window.title("View Student")
        view_window.geometry("400x300")

        tk.Label(view_window, text="Enter Roll Number").pack()

        roll_entry = tk.Entry(view_window)
        roll_entry.pack()

        def search_student():
            try:
                roll_no = int(roll_entry.get())
            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Roll number must be a number."
                )
                return

            student = get_student(roll_no)

            if student:
                result = (
                    f"Roll Number: {student.roll_no}\n"
                    f"Name: {student.name}\n"
                    f"Marks: {student.marks}\n"
                    f"Average: {student.average():.2f}"
                )

                tk.Label(view_window, text=result).pack(pady=20)

            else:
                messagebox.showerror(
                    "Not Found",
                    "Student not found!"
                )

        tk.Button(
            view_window,
            text="Search",
            command=search_student
        ).pack(pady=20)


    def view_all_students_ui():

        all_window = tk.Toplevel(window)
        all_window.title("All Students")
        all_window.geometry("600x400")

        students = get_all_students()

        if not students:
            tk.Label(
                all_window,
                text="No students found!"
            ).pack(pady=30)

            return

        listbox = tk.Listbox(
            all_window,
            width=70,
            height=20
        )

        listbox.pack(
            padx=20,
            pady=20
        )

        for student in students:

            text = (
                f"Roll No: {student.roll_no} | "
                f"Name: {student.name} | "
                f"Marks: {student.marks} | "
                f"Average: {student.average():.2f}"
            )

            listbox.insert(
                tk.END,
                text
            )

    def update_student_ui():
        update_window = tk.Toplevel(window)
        update_window.title("Update Student")
        update_window.geometry("400x350")

        tk.Label(update_window, text="Enter Roll Number").pack()

        roll_entry = tk.Entry(update_window)
        roll_entry.pack()

        def load_student():
            try:
                roll_no = int(roll_entry.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Roll number must be a number.")
                return

            student = get_student(roll_no)

            if not student:
                messagebox.showerror("Not Found", "Student not found!")
                return

            tk.Label(update_window, text="New Name").pack()
            name_entry = tk.Entry(update_window)
            name_entry.insert(0, student.name)
            name_entry.pack()

            tk.Label(update_window, text="New Marks").pack()
            marks_entry = tk.Entry(update_window)
            marks_entry.insert(0, " ".join(map(str, student.marks)))
            marks_entry.pack()

            def submit_update():
                new_name = name_entry.get()
                new_marks = list(map(int, marks_entry.get().split()))

                update_student(
                    roll_no,
                    new_name,
                    new_marks
                )

                save_students()

                messagebox.showinfo(
                    "Success",
                    "Student updated successfully!"
                )

            tk.Button(
                update_window,
                text="Update",
                command=submit_update
            ).pack(pady=20)

        tk.Button(
            update_window,
            text="Find Student",
            command=load_student
        ).pack(pady=20)

    def delete_student_ui():
        delete_window = tk.Toplevel(window)
        delete_window.title("Delete Student")
        delete_window.geometry("400x250")

        tk.Label(delete_window, text="Enter Roll Number").pack()

        roll_entry = tk.Entry(delete_window)
        roll_entry.pack()

        def confirm_delete():

            try:
                roll_no = int(roll_entry.get())

            except ValueError:

                messagebox.showerror(
                    "Invalid Input",
                    "Roll number must be a number."
                )

                return

            student = get_student(roll_no)

            if not student:

                messagebox.showerror(
                    "Not Found",
                    "Student not found!"
                )

                return

            confirm = messagebox.askyesno(
                "Confirm Delete",
                f"Delete student {student.name}?"
            )

            if confirm:

                delete_student(roll_no)
                save_students()

                messagebox.showinfo(
                    "Success",
                    "Student deleted successfully!"
                )

                delete_window.destroy()

        tk.Button(
            delete_window,
            text="Delete",
            command=confirm_delete
        ).pack(pady=20)

        # Title
    title = tk.Label(
        window,
        text="Student Management System",
        font=("Arial", 20)
    )
    title.pack(pady=30)


    # Button container
    button_frame = tk.Frame(window)
    button_frame.pack()


    # Buttons
    add_button = tk.Button(
        button_frame,
        text="Add Student",
        width=20,
        command=add_student_ui
    )
    add_button.grid(row=0, column=0, padx=10, pady=10)


    view_button = tk.Button(
        button_frame,
        text="View Student",
        width=20,
        command=view_student_ui
    )
    view_button.grid(row=0, column=1, padx=10, pady=10)


    view_all_button = tk.Button(
        button_frame,
        text="View All Students",
        width=20,
        command=view_all_students_ui
    )
    view_all_button.grid(row=1, column=0, padx=10, pady=10)


    update_button = tk.Button(
        button_frame,
        text="Update Student",
        width=20,
        command=update_student_ui
    )
    update_button.grid(row=1, column=1, padx=10, pady=10)


    delete_button = tk.Button(
        button_frame,
        text="Delete Student",
        width=20,
        command=delete_student_ui
    )
    delete_button.grid(row=2, column=0, padx=10, pady=10)
    window.mainloop()