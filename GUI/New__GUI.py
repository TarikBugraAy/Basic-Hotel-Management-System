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

# Function to clear existing management frames
def clear_management_frames(panel):
    x_panel = panel
    for widget in x_panel.grid_slaves(row=1, column=0):
        widget.destroy()

# Function to display manage staff options
def manage_staff_options():
    clear_management_frames(admin_panel)
    manage_staff_frame = tk.Frame(admin_panel)
    manage_staff_frame.grid(row=1, column=0, columnspan=7, pady=10)

    manage_staff_lframe = tk.LabelFrame(manage_staff_frame,padx=10,pady=0)
    manage_staff_lframe.grid(row=1, column=0, columnspan=7, pady=10)

    add_staff_button = tk.Button(manage_staff_lframe, text="Add Staff", font=("Times New Roman", 12), command=None)
    add_staff_button.grid(row=0, column=0, padx=10, pady=10)

    delete_staff_button = tk.Button(manage_staff_lframe, text="Delete Staff", font=("Times New Roman", 12), command=None)
    delete_staff_button.grid(row=0, column=1, padx=10, pady=10)

    update_staff_button = tk.Button(manage_staff_lframe, text="Update Staff", font=("Times New Roman", 12), command=None)
    update_staff_button.grid(row=0, column=2, padx=10, pady=10)

    view_staff_button = tk.Button(manage_staff_lframe, text="View Staff", font=("Times New Roman", 12), command=None)
    view_staff_button.grid(row=0, column=3, padx=10, pady=10)


def manage_rooms_options(x_frame):
    frame_panel = x_frame
    clear_management_frames(frame_panel)
    manage_rooms_frame = tk.Frame(frame_panel)
    manage_rooms_frame.grid(row=1, column=0, columnspan=7, pady=10)

    manage_rooms_lframe = tk.LabelFrame(manage_rooms_frame, padx=10, pady=0)
    manage_rooms_lframe.grid(row=1, column=0, columnspan=7, pady=10)

    add_room_button = tk.Button(manage_rooms_lframe, text="Add Room", font=("Times New Roman", 12), command=None)
    add_room_button.grid(row=0, column=0, padx=10, pady=10)

    delete_room_button = tk.Button(manage_rooms_lframe, text="Delete Room", font=("Times New Roman", 12), command=None)
    delete_room_button.grid(row=0, column=1, padx=10, pady=10)

    update_room_button = tk.Button(manage_rooms_lframe, text="Update Room", font=("Times New Roman", 12), command=None)
    update_room_button.grid(row=0, column=2, padx=10, pady=10)

    view_room_button = tk.Button(manage_rooms_lframe, text="View Rooms", font=("Times New Roman", 12), command=None)
    view_room_button.grid(row=0, column=3, padx=10, pady=10)

#Manage Reservations Options
def manage_reservations_options(x_frame):
    frame_panel=x_frame
    clear_management_frames(frame_panel)

    manage_reservations_frame=tk.Frame(frame_panel)
    manage_reservations_frame.grid(row=1,column=0,columnspan=7,pady=10)

    manage_reservations_lframe = tk.LabelFrame(manage_reservations_frame,padx=10,pady=10)
    manage_reservations_lframe.grid(row=1, column=0, columnspan=7, pady=10)

    add_reservations_button = tk.Button(manage_reservations_lframe, text="Add Reservations", font=("Times New Roman", 12), command=None)
    add_reservations_button.grid(row=0,column=0, padx=10, pady=10)

    delete_reservations_button = tk.Button(manage_reservations_lframe, text="Delete Reservations",font=("Times New Roman", 12), command=None)
    delete_reservations_button.grid(row=0,column=1,padx=10,pady=10)

    update_reservations_button = tk.Button(manage_reservations_lframe, text="Update Reservations",font=("Times New Roman", 12), command=None)
    update_reservations_button.grid(row=0, column=2, padx=10,pady=10)

# Function to manage login logs
def manage_login_logs():
    clear_management_frames(admin_panel)
    manage_logs_frame = tk.Frame(admin_panel)
    manage_logs_frame.grid(row=1, column=0, columnspan=7, pady=10)

    manage_logs_lframe = tk.LabelFrame(manage_logs_frame, text="Login Logs", padx=10, pady=10, font=("Times New Roman", 12))
    manage_logs_lframe.grid(row=1, column=0, columnspan=7, pady=10)

    logs_text = tk.Text(manage_logs_lframe, height=20, width=100, font=("Times New Roman", 12))
    logs_text.grid(row=0, column=0, padx=10, pady=10)

    scrollbar = tk.Scrollbar(manage_logs_lframe, command=logs_text.yview)
    logs_text.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='nsew')

    cursor = project_db.cursor()
    cursor.execute("SELECT u.name, u.role, l.login_time FROM log l JOIN users u ON l.user_id = u.user_id ORDER BY l.login_time DESC")
    logs = cursor.fetchall()

    for log in logs:
        logs_text.insert(tk.END, f"Name: {log[0]}, Role: {log[1]}, Login Time: {log[2]}\n")


# Open Admin Panel
def open_admin_panel():
    global admin_panel

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
    manage_staff = tk.Button(admin_frame, text="Manage Staff", font=("Times New Roman", 12), command=manage_staff_options)
    manage_staff.grid(row=0, column=0, padx=10, pady=10)

    manage_rooms = tk.Button(admin_frame, text="Manage Rooms", font=("Times New Roman", 12), command=lambda:manage_rooms_options(admin_panel))
    manage_rooms.grid(row=0, column=1, padx=10, pady=10)

    manage_reservations = tk.Button(admin_frame, text="Manage Reservations", font=("Times New Roman", 12), command=lambda:manage_reservations_options(admin_panel))
    manage_reservations.grid(row=0, column=2, padx=10, pady=10)

    manage_payments = tk.Button(admin_frame, text="Manage Payments", font=("Times New Roman", 12), command=None)
    manage_payments.grid(row=0, column=3, padx=10, pady=10)

    manage_maintenance = tk.Button(admin_frame, text="Manage Maintenance", font=("Times New Roman", 12), command=None)
    manage_maintenance.grid(row=0, column=4, padx=10, pady=10)

    manage_reports = tk.Button(admin_frame, text="Manage Reports", font=("Times New Roman", 12), command=None)
    manage_reports.grid(row=0, column=5, padx=10, pady=10)

    manage_logs = tk.Button(admin_frame, text="Manage Logs", font=("Times New Roman", 12), command=manage_login_logs)
    manage_logs.grid(row=0, column=6, padx=10, pady=10)

    admin_panel.mainloop()

# Open Staff Panel
def open_staff_panel():
    global staff_panel
    login_window.destroy()
    staff_panel = tk.Tk()
    staff_panel.title("Hotel Management System - Staff Panel")

    width = 650
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
    manage_rooms = tk.Button(staff_frame, text="Manage Rooms", font=("Times New Roman", 12), command=lambda:manage_rooms_options(staff_panel))
    manage_rooms.grid(row=0, column=1, padx=10, pady=10)

    manage_reservations = tk.Button(staff_frame, text="Manage Reservations", font=("Times New Roman", 12), command=lambda:manage_reservations_options(staff_panel))
    manage_reservations.grid(row=0, column=2, padx=10, pady=10)

    manage_payments = tk.Button(staff_frame, text="Manage Payments", font=("Times New Roman", 12), command=None)
    manage_payments.grid(row=0, column=3, padx=10, pady=10)

    manage_maintenance = tk.Button(staff_frame, text="Manage Maintenance", font=("Times New Roman", 12), command=None)
    manage_maintenance.grid(row=0, column=4, padx=10, pady=10)

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
