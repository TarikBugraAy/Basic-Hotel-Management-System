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

# Function to clear existing management frames
def clear_management_frames():
    for widget in admin_panel.grid_slaves(row=1, column=0):
        widget.destroy()

# Function to display manage staff options
def manage_staff_options():
    clear_management_frames()
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


def manage_rooms_options():
    clear_management_frames()
    manage_rooms_frame = tk.Frame(admin_panel)
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

# Open Admin Panel
def open_admin_panel():
    global admin_panel


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

    manage_rooms = tk.Button(admin_frame, text="Manage Rooms", font=("Times New Roman", 12), command=manage_rooms_options)
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