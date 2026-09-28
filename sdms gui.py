import tkinter as tk

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

title = tk.Label(
    window,
    text="Student Management System",
    font=("Arial", 20)
)

title.pack(pady=30)

add_button = tk.Button(
    window,
    text="Add Student",
    command=add_student_ui
)

add_button.pack()

window.mainloop()