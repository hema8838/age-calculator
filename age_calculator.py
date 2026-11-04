import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        dob = date(year, month, day)
        
        today = date.today()

        if dob > today:
            messagebox.showerror("Error", "Invalid Date of Birth")
            return

        age = today.year - dob.year

        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1

        result_label.config(text=f"Your Age is: {age} years")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid date!")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x450")
root.configure(bg="pink")

heading = tk.Label(
    root,
    text="AGE CALCULATOR",
    font=("Arial", 20, "bold"),
    bg="light yellow",
    fg="purple"
)
heading.pack(pady=20)

tk.Label(root, text="Enter Day", bg="lavender").pack()
day_entry = tk.Entry(root)
day_entry.pack(pady=5)

tk.Label(root, text="Enter Month", bg="lavender").pack()
month_entry = tk.Entry(root)
month_entry.pack(pady=5)

tk.Label(root, text="Enter Year", bg="lavender").pack()
year_entry = tk.Entry(root)
year_entry.pack(pady=5)

calculate_button = tk.Button(
    root,
    text="Calculate Age",
    command=calculate_age,
    bg="purple",
    fg="white",
    activebackground="blue",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    cursor="hand2"
)
calculate_button.pack(pady=20)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 15, "bold"),
    bg="lavender",
    fg="green"
)
result_label.pack(pady=10)

root.mainloop()