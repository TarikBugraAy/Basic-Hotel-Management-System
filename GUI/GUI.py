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
        database="HotelManagementSystem"
    )
    print("Connected to the database successfully.")
except mysql.connector.Error as err:
    print(f"Error connecting to the database: {err}")

# Function to handle the login button click
def login():
    username = entry_username.get()
    password = entry_password.get()

    user_type, name = verify_login(username, password)

    if user_type:
        messagebox.showinfo("Login Success", f"Welcome {name} ({user_type})")
        if user_type == 'admin':
            # Open admin panel
            open_admin_panel()
        else:
            # Open staff panel
            open_staff_panel()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to verify the user's credentials
def verify_login(username, password):
    cursor = project_db.cursor(dictionary=True)

    # Check in the Admin table
    query = "SELECT * FROM Admin WHERE username = %s"
    cursor.execute(query, (username,))
    admin = cursor.fetchone()
    if admin and password == admin['password']:
        log_login(admin['admin_id'], admin['name'], 'admin')
        return 'admin', admin['name']

    # Check in the Staff table
    query = "SELECT * FROM Staff WHERE username = %s"
    cursor.execute(query, (username,))
    staff = cursor.fetchone()
    if staff and password == staff['password']:
        log_login(staff['staff_id'], staff['name'], 'staff')
        return 'staff', staff['name']

    cursor.close()
    return None, None

# Function to log the login attempts
def log_login(user_id, name, user_type):
    cursor = project_db.cursor()
    login_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO Log (user_id, name, user_type, login_time) VALUES (%s, %s, %s, %s)"
    values = (user_id, name, user_type, login_time)
    cursor.execute(query, values)
    project_db.commit()
    cursor.close()

# Function to show the manage rooms panel
def show_manage_rooms_panel():
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="Manage Rooms", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=20)

    tk.Button(content_frame, text="Add Room", command=add_room).grid(row=1, column=0, pady=5)
    tk.Button(content_frame, text="Delete Room", command=delete_room).grid(row=1, column=1, pady=5)
    tk.Button(content_frame, text="Update Room Status", command=update_room_status).grid(row=2, column=0, pady=5)
    tk.Button(content_frame, text="View Rooms", command=view_rooms).grid(row=2, column=1, pady=5)

# Function to add a new room
def add_room():
    for widget in content_frame.winfo_children():
        widget.destroy()

    def save_room():
        room_number = entry_room_number.get()
        room_type = entry_room_type.get()
        room_status = entry_room_status.get()
        cursor = project_db.cursor()
        query = "INSERT INTO Rooms (room_number, type, status) VALUES (%s, %s, %s)"
        values = (room_number, room_type, room_status)
        cursor.execute(query, values)
        project_db.commit()
        cursor.close()
        messagebox.showinfo("Success", "Room added successfully")
        show_manage_rooms_panel()

    tk.Label(content_frame, text="Add New Room").grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(content_frame, text="Room Number").grid(row=1, column=0)
    entry_room_number = tk.Entry(content_frame)
    entry_room_number.grid(row=1, column=1)

    tk.Label(content_frame, text="Room Type").grid(row=2, column=0)
    entry_room_type = tk.Entry(content_frame)
    entry_room_type.grid(row=2, column=1)

    tk.Label(content_frame, text="Room Status").grid(row=3, column=0)
    entry_room_status = tk.Entry(content_frame)
    entry_room_status.grid(row=3, column=1)

    tk.Button(content_frame, text="Save", command=save_room).grid(row=4, column=0, columnspan=2, pady=20)

# Function to delete a room
def delete_room():
    for widget in content_frame.winfo_children():
        widget.destroy()

    def confirm_delete():
        room_number = entry_room_number.get()
        cursor = project_db.cursor()
        query = "DELETE FROM Rooms WHERE room_number = %s"
        cursor.execute(query, (room_number,))
        project_db.commit()
        cursor.close()
        messagebox.showinfo("Success", "Room deleted successfully")
        show_manage_rooms_panel()

    tk.Label(content_frame, text="Delete Room").grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(content_frame, text="Room Number").grid(row=1, column=0)
    entry_room_number = tk.Entry(content_frame)
    entry_room_number.grid(row=1, column=1)

    tk.Button(content_frame, text="Delete", command=confirm_delete).grid(row=2, column=0, columnspan=2, pady=20)

# Function to update room status
def update_room_status():
    for widget in content_frame.winfo_children():
        widget.destroy()

    def save_status():
        room_number = entry_room_number.get()
        new_status = entry_new_status.get()
        cursor = project_db.cursor()
        query = "UPDATE Rooms SET status = %s WHERE room_number = %s"
        cursor.execute(query, (new_status, room_number))
        project_db.commit()
        cursor.close()
        messagebox.showinfo("Success", "Room status updated successfully")
        show_manage_rooms_panel()

    tk.Label(content_frame, text="Update Room Status").grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(content_frame, text="Room Number").grid(row=1, column=0)
    entry_room_number = tk.Entry(content_frame)
    entry_room_number.grid(row=1, column=1)

    tk.Label(content_frame, text="New Status").grid(row=2, column=0)
    entry_new_status = tk.Entry(content_frame)
    entry_new_status.grid(row=2, column=1)

    tk.Button(content_frame, text="Save", command=save_status).grid(row=3, column=0, columnspan=2, pady=20)

# Function to view all rooms
def view_rooms():
    for widget in content_frame.winfo_children():
        widget.destroy()

    cursor = project_db.cursor()
    cursor.execute("SELECT * FROM Rooms")
    rooms = cursor.fetchall()
    cursor.close()

    tk.Label(content_frame, text="Rooms", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    for idx, room in enumerate(rooms, start=1):
        tk.Label(content_frame, text=f"Room Number: {room[1]}, Type: {room[2]}, Status: {room[3]}").grid(row=idx, column=0, columnspan=2)

# Function to view room status
def view_room_status():
    for widget in content_frame.winfo_children():
        widget.destroy()

    cursor = project_db.cursor()
    cursor.execute("SELECT room_number, status FROM Rooms")
    rooms = cursor.fetchall()
    cursor.close()

    tk.Label(content_frame, text="Room Status", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    for idx, room in enumerate(rooms, start=1):
        tk.Label(content_frame, text=f"Room Number: {room[0]}, Status: {room[1]}").grid(row=idx, column=0, columnspan=2)

# Function to view room details
def view_room_details():
    for widget in content_frame.winfo_children():
        widget.destroy()

    cursor = project_db.cursor()
    cursor.execute("SELECT * FROM Rooms")
    rooms = cursor.fetchall()
    cursor.close()

    tk.Label(content_frame, text="Room Details", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

    for idx, room in enumerate(rooms, start=1):
        tk.Label(content_frame, text=f"Room Number: {room[1]}").grid(row=idx, column=0)
        tk.Label(content_frame, text=f"Type: {room[2]}").grid(row=idx, column=1)
        tk.Label(content_frame, text=f"Status: {room[3]}").grid(row=idx, column=2)

# Function to request maintenance
def request_maintenance():
    for widget in content_frame.winfo_children():
        widget.destroy()

    def submit_request():
        room_number = entry_room_number.get()
        issue_description = entry_issue_description.get("1.0", "end-1c")
        cursor = project_db.cursor()
        query = "INSERT INTO MaintenanceRequests (room_number, issue_description, status) VALUES (%s, %s, 'Pending')"
        values = (room_number, issue_description)
        cursor.execute(query, values)
        project_db.commit()
        cursor.close()
        messagebox.showinfo("Success", "Maintenance request submitted successfully")
        show_manage_rooms_panel()

    tk.Label(content_frame, text="Request Maintenance").grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(content_frame, text="Room Number").grid(row=1, column=0)
    entry_room_number = tk.Entry(content_frame)
    entry_room_number.grid(row=1, column=1)

    tk.Label(content_frame, text="Issue Description").grid(row=2, column=0)
    entry_issue_description = tk.Text(content_frame, height=5, width=40)
    entry_issue_description.grid(row=2, column=1)

    tk.Button(content_frame, text="Submit", command=submit_request).grid(row=3, column=0, columnspan=2, pady=20)

# Function to open the admin panel
def open_admin_panel():
    global admin_panel, content_frame

    # Close the login window
    login_window.destroy()
    admin_panel = tk.Tk()
    admin_panel.title("Admin Panel")

    # Set dimensions and center the window
    width = 800
    height = 600
    screen_width = admin_panel.winfo_screenwidth()
    screen_height = admin_panel.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    admin_panel.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    # Define the structure of the admin panel
    nav_frame = tk.Frame(admin_panel)
    nav_frame.grid(row=0, column=0, sticky="ns")

    content_frame = tk.Frame(admin_panel)
    content_frame.grid(row=0, column=1, sticky="nsew")

    admin_panel.grid_columnconfigure(1, weight=1)
    admin_panel.grid_rowconfigure(0, weight=1)

    tk.Label(nav_frame, text="Admin Panel", font=("Helvetica", 16)).grid(row=0, column=0, pady=20)

    tk.Button(nav_frame, text="Manage Rooms", command=show_manage_rooms_panel).grid(row=1, column=0, pady=5)
    tk.Button(nav_frame, text="Manage Reservations").grid(row=2, column=0, pady=5)
    tk.Button(nav_frame, text="Process Billing").grid(row=3, column=0, pady=5)
    tk.Button(nav_frame, text="Manage Staff").grid(row=4, column=0, pady=5)
    tk.Button(nav_frame, text="Handle Maintenance").grid(row=5, column=0, pady=5)
    tk.Button(nav_frame, text="Manage Inventory").grid(row=6, column=0, pady=5)
    tk.Button(nav_frame, text="Generate Reports").grid(row=7, column=0, pady=5)

    admin_panel.mainloop()

# Function to open the staff panel
def open_staff_panel():
    global staff_panel, content_frame

    # Close the login window
    login_window.destroy()
    staff_panel = tk.Tk()
    staff_panel.title("Staff Panel")

    # Set dimensions and center the window
    width = 800
    height = 600
    screen_width = staff_panel.winfo_screenwidth()
    screen_height = staff_panel.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    staff_panel.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    # Define the structure of the staff panel
    nav_frame = tk.Frame(staff_panel)
    nav_frame.grid(row=0, column=0, sticky="ns")

    content_frame = tk.Frame(staff_panel)
    content_frame.grid(row=0, column=1, sticky="nsew")

    staff_panel.grid_columnconfigure(1, weight=1)
    staff_panel.grid_rowconfigure(0, weight=1)

    tk.Label(nav_frame, text="Staff Panel", font=("Helvetica", 16)).grid(row=0, column=0, pady=20)

    tk.Button(nav_frame, text="View Room Status", command=view_room_status).grid(row=1, column=0, pady=5)
    tk.Button(nav_frame, text="Update Room Status", command=update_room_status).grid(row=2, column=0, pady=5)
    tk.Button(nav_frame, text="View Room Details", command=view_room_details).grid(row=3, column=0, pady=5)
    tk.Button(nav_frame, text="Request Maintenance", command=request_maintenance).grid(row=4, column=0, pady=5)

    staff_panel.mainloop()

# Main login window
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

login_frame = tk.LabelFrame(login_window, padx=10, pady=10, text="Login")
login_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)

# Username Label and Entry
tk.Label(login_frame, text="Username").grid(row=0, column=0, pady=10, padx=10)
entry_username = tk.Entry(login_frame)
entry_username.grid(row=0, column=1, pady=10, padx=10)

# Password Label and Entry
tk.Label(login_frame, text="Password").grid(row=1, column=0, pady=10, padx=10)
entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=1, column=1, pady=10, padx=10)

# Login Button
tk.Button(login_frame, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=20)

login_window.mainloop()
