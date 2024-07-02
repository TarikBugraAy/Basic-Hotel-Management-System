import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

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



# Function to open the admin panel
def open_admin_panel():
    # Close the login window
    login_window.destroy()
    admin_panel = tk.Tk()
    admin_panel.title("Admin Panel")

    # Set dimensions and center the window
    width = 400
    height = 400
    screen_width = admin_panel.winfo_screenwidth()
    screen_height = admin_panel.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    admin_panel.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    # Define the structure of the admin panel
    label = tk.Label(admin_panel, text="Admin Panel", font=("Helvetica", 16))
    label.pack(pady=20)

    button_manage_rooms = tk.Button(admin_panel, text="Manage Rooms")
    button_manage_rooms.pack(pady=5)

    button_manage_reservations = tk.Button(admin_panel, text="Manage Reservations")
    button_manage_reservations.pack(pady=5)

    button_process_billing = tk.Button(admin_panel, text="Process Billing")
    button_process_billing.pack(pady=5)

    button_manage_staff = tk.Button(admin_panel, text="Manage Staff")
    button_manage_staff.pack(pady=5)

    button_handle_maintenance = tk.Button(admin_panel, text="Handle Maintenance")
    button_handle_maintenance.pack(pady=5)

    button_manage_inventory = tk.Button(admin_panel, text="Manage Inventory")
    button_manage_inventory.pack(pady=5)

    button_generate_reports = tk.Button(admin_panel, text="Generate Reports")
    button_generate_reports.pack(pady=5)

    admin_panel.mainloop()

# Function to open the staff panel
def open_staff_panel():
    # Close the login window
    login_window.destroy()
    staff_panel = tk.Tk()
    staff_panel.title("Staff Panel")

    # Set dimensions and center the window
    width = 400
    height = 400
    screen_width = staff_panel.winfo_screenwidth()
    screen_height = staff_panel.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    staff_panel.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    # Define the structure of the staff panel
    label = tk.Label(staff_panel, text="Staff Panel", font=("Helvetica", 16))
    label.pack(pady=20)

    button_manage_reservations = tk.Button(staff_panel, text="Manage Reservations")
    button_manage_reservations.pack(pady=5)

    button_process_billing = tk.Button(staff_panel, text="Process Billing")
    button_process_billing.pack(pady=5)

    button_handle_maintenance = tk.Button(staff_panel, text="Handle Maintenance")
    button_handle_maintenance.pack(pady=5)

    button_manage_inventory = tk.Button(staff_panel, text="Manage Inventory")
    button_manage_inventory.pack(pady=5)

    staff_panel.mainloop()

# Create the login window
login_window = tk.Tk()
login_window.title("Hotel Management System - Login")

# Set dimensions and center the window
width = 325
height = 275
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
login_window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

label_frame = tk.LabelFrame(login_window, text="Login", font=("Helvetica", 16), padx=60, pady=60, borderwidth=2, relief="groove")
label_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", )

label_username = tk.Label(label_frame, text="Username")
label_username.grid(row=0, column=0, pady=5)
entry_username = tk.Entry(label_frame)
entry_username.grid(row=0, column=1, pady=5)

label_password = tk.Label(label_frame, text="Password")
label_password.grid(row=1, column=0, pady=5)
entry_password = tk.Entry(label_frame, show="*")
entry_password.grid(row=1, column=1, pady=5)

button_login = tk.Button(label_frame, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2, pady=5)

login_window.mainloop()
