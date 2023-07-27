import tkinter as tk
from tkinter import ttk
import json

def show_win1():
    win2.pack_forget()  # Hide win2
    win1.pack(fill=tk.BOTH, expand=True)  # Show win1

def show_win2():
    win1.pack_forget()  # Hide win1
    win2.pack(fill=tk.BOTH, expand=True)  # Show win2
    update_list()

def add_emp():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    salary = salary_entry.get()  # New input for salary

    if name and age and email and salary:
        emp = {"name": name, "age": int(age), "email": email, "salary": float(salary)}  # Convert salary to float
        data.append(emp)
        update_list()
        save_json()

def del_emp():
    sel_item = tree.focus()
    if sel_item:
        index = tree.index(sel_item)
        data.pop(index)
        update_list()
        save_json()

def update_list():
    tree.delete(*tree.get_children())  # Clear the Treeview
    for item in data:
        tree.insert("", "end", values=(item["name"], item["age"], item["email"], item["salary"]))  # Display salary

def save_json():
    with open("employees.json", "w") as f:
        json.dump(data, f)

def load_json():
    try:
        with open("employees.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def close():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Employee Management System")

# Set the window size and center it on the screen
w_width = 800
w_height = 600
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
x_offset = (s_width - w_width) // 2
y_offset = (s_height - w_height) // 2
root.geometry(f"{w_width}x{w_height}+{x_offset}+{y_offset}")

# Create a frame for the buttons and place it at the top of the window
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(fill=tk.X, padx=10, pady=10)

# Create buttons to switch between windows inside the btn_frame
btn1 = tk.Button(btn_frame, text="Add Employees", command=show_win1, padx=10, pady=5)
btn1.pack(side=tk.LEFT)

btn2 = tk.Button(btn_frame, text="Manage Employees", command=show_win2, padx=10, pady=5)
btn2.pack(side=tk.LEFT)

# Create a style for Treeview widget
style = ttk.Style(root)
style.theme_use("clam")  # Choose one of the available themes (e.g., clam)

style.configure("Treeview", font=("Arial", 12), rowheight=25, background="#f0f0f0")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

# Create the first window/frame for employee management controls
win1 = tk.Frame(root, bg="#f0f0f0")

name_lbl = tk.Label(win1, text="Name:", font=("Arial", 14, "bold"), bg="#f0f0f0")
name_lbl.pack(pady=5)
name_entry = tk.Entry(win1, font=("Arial", 12))
name_entry.pack(pady=5)

age_lbl = tk.Label(win1, text="Age:", font=("Arial", 14, "bold"), bg="#f0f0f0")
age_lbl.pack(pady=5)
age_entry = tk.Entry(win1, font=("Arial", 12))
age_entry.pack(pady=5)

email_lbl = tk.Label(win1, text="Email:", font=("Arial", 14, "bold"), bg="#f0f0f0")
email_lbl.pack(pady=5)
email_entry = tk.Entry(win1, font=("Arial", 12))
email_entry.pack(pady=5)

salary_lbl = tk.Label(win1, text="Salary:", font=("Arial", 14, "bold"), bg="#f0f0f0")
salary_lbl.pack(pady=5)
salary_entry = tk.Entry(win1, font=("Arial", 12))
salary_entry.pack(pady=5)

add_btn = tk.Button(win1, text="Add Employee", command=add_emp, font=("Arial", 12), bg="#2196f3", fg="white")
add_btn.pack(pady=10)

del_btn = tk.Button(win1, text="Close", command=close, font=("Arial", 12), bg="#f44336", fg="white")
del_btn.pack(pady=10)

# Create the second window/frame for displaying the employee list
win2 = tk.Frame(root, bg="#f0f0f0")

# Add a spreadsheet-like interface using Treeview widget on win2
columns = ("Name", "Age", "Email", "Salary")  # Add "Salary" column
tree = ttk.Treeview(win2, columns=columns, show="headings", selectmode="browse")

# Set column headings
for col in columns:
    tree.heading(col, text=col)

tree.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

del_lbl = tk.Label(win2, text="Hit Delete to Remove Selected Employees")
del_lbl.pack(pady=10)

# Sample data for the employee list (loaded from the JSON file)
data = load_json()

# Initially show win1 and hide win2
win1.pack(fill=tk.BOTH, expand=True)
win2.pack_forget()

# Bind the del_emp function to the Delete key
tree.bind("<Delete>", lambda event: del_emp())

# Start the tkinter main loop
root.mainloop()