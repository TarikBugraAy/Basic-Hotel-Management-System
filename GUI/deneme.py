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


# Open Admin Panel
def open_admin_panel():

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
    
open_admin_panel()