import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import *

# Connect to your MySQL database
try:
    project_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tarik7172",
        port="3306",
        database="HMS"
    )
    print("Connected to the database successfully.")
except mysql.connector.Error as err:
    print(f"Error connecting to the database: {err}")

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()

    user_type, name = verify_login(username, password)

    if user_type:
        messagebox.showinfo("Login Success", f"Welcome {name} ({user_type})")
        if user_type == 'admin':
            open_admin_panel()
        else:
            open_staff_panel()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Verify Login Function
def verify_login(username, password):
    cursor = project_db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cursor.fetchone()

    if user:
        log_login(username)
        return user[2], user[1]
    else:
        return None, None

# Log logins to the database
def log_login(username):
    cursor = project_db.cursor()
    cursor.execute(f"SELECT user_id FROM users WHERE username = '{username}'")
    user_id = cursor.fetchone()[0]  # Extracting the integer value from the tuple
    cursor.execute(f"INSERT INTO log (user_id, login_time) VALUES ({user_id}, '{datetime.now()}')")
    project_db.commit()

# Open Admin Panel
def open_admin_panel():
    login_window.destroy()
    admin_panel = tk.Tk()
    admin_panel.title("Hotel Management System - Admin Panel")

    # Setting dimentions of the panel
    width = 1014
    height = 600
    screen_width = admin_panel.winfo_screenwidth()
    screen_height = admin_panel.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    admin_panel.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    # Defining the main frame of the admin panel
    admin_frame = tk.LabelFrame(admin_panel, padx=10, pady=10, font=("Times New Roman", 12))
    admin_frame.grid(row=0, column=0, padx=10, pady=10)

    # Defining the buttons
    manage_staff = tk.Button(admin_frame, text="Manage Staff", font=("Times New Roman", 12), command=None)
    manage_staff.grid(row=0, column=0, padx=10, pady=10)

    manage_rooms = tk.Button(admin_frame, text="Manage Rooms", font=("Times New Roman", 12), command=None)
    manage_rooms.grid(row=0, column=1, padx=10, pady=10)

    manage_reservations = tk.Button(admin_frame, text="Manage Reservations", font=("Times New Roman", 12), command=None)
    manage_reservations.grid(row=0, column=2, padx=10, pady=10)

    manage_payments = tk.Button(admin_frame, text="Manage Payments", font=("Times New Roman", 12), command=None)
    manage_payments.grid(row=0, column=3, padx=10, pady=10)

    manage_maintenance = tk.Button(admin_frame, text="Manage Maintenance", font=("Times New Roman", 12), command=None)
    manage_maintenance.grid(row=0, column=4, padx=10, pady=10)

    manage_reports = tk.Button(admin_frame, text="Manage Reports", font=("Times New Roman", 12), command=None)
    manage_reports.grid(row=0, column=5, padx=10, pady=10)

    manage_logs = tk.Button(admin_frame, text="Manage Logs", font=("Times New Roman", 12), command=None)
    manage_logs.grid(row=0, column=6, padx=10, pady=10)

    admin_panel.mainloop()

# Open Staff Panel
def open_staff_panel():
    login_window.destroy()
    staff_panel = tk.Tk()
    staff_panel.title("Hotel Management System - Staff Panel")

    width = 1000
    height = 600
    screen_width = staff_panel.winfo_screenwidth()
    screen_height = staff_panel.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    staff_panel.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    # Defining the main frame of the staff panel
    staff_frame = tk.LabelFrame(staff_panel, padx=10, pady=10, font=("Times New Roman", 12))
    staff_frame.grid(row=0, column=0, padx=10, pady=10)

    # Defining the buttons
    

    staff_panel.mainloop()

# Login Window
login_window = tk.Tk()
login_window.title("Hotel Management System - Login")

# Set dimensions and center the window
width = 350
height = 300
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
login_window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

login_frame = tk.LabelFrame(login_window, text="Login", padx=10, pady=10, font=("Times New Roman", 12))
login_frame.grid(row=0, column=0, padx=10, pady=10)

# Username Label and Entry
username_label = tk.Label(login_frame, text="Username:", font=("Times New Roman", 12))
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_frame, font=("Times New Roman", 12))
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password Label and Entry
password_label = tk.Label(login_frame, text="Password:", font=("Times New Roman", 12))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_frame, show="*", font=("Times New Roman", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login Button
login_button = tk.Button(login_frame, text="Login", font=("Times New Roman", 12), command=login, bg="blue", fg="white")
login_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

login_window.mainloop()
