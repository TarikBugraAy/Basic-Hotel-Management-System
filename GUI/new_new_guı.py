import mysql.connector

class Database:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def verify_user(self, username, password):
        cursor = self.connection.cursor()
        query = "SELECT user_id, name, role FROM Users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()
        return user

    def log_user_login(self, user_id):
        cursor = self.connection.cursor()
        query = "INSERT INTO Log (user_id, login_time) VALUES (%s, NOW())"
        cursor.execute(query, (user_id,))
        self.connection.commit()
        cursor.close()

import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, db):
        self.db = db
        self.login_window = tk.Tk()
        self.setup_login_window()

    def setup_login_window(self):
        self.login_window.title("Hotel Management System - Login")

        width = 400
        height = 300
        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.login_window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        tk.Label(self.login_window, text="Username", font=("Times New Roman", 14)).pack(pady=10)
        self.username_entry = tk.Entry(self.login_window, font=("Times New Roman", 14))
        self.username_entry.pack(pady=10)

        tk.Label(self.login_window, text="Password", font=("Times New Roman", 14)).pack(pady=10)
        self.password_entry = tk.Entry(self.login_window, show='*', font=("Times New Roman", 14))
        self.password_entry.pack(pady=10)

        login_button = tk.Button(self.login_window, text="Login", font=("Times New Roman", 14), command=self.login)
        login_button.pack(pady=20)

        self.login_window.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.db.verify_user(username, password)

        if user:
            user_id, name, role = user
            self.db.log_user_login(user_id)
            self.login_window.destroy()
            if role == 'admin':
                AdminPanel(self.db)
            elif role == 'staff':
                StaffPanel(self.db)
        else:
            messagebox.showerror("Error", "Invalid username or password")

import tkinter as tk

class AdminPanel:
    def __init__(self, db):
        self.db = db
        self.admin_panel = tk.Tk()
        self.setup_admin_panel()

    def setup_admin_panel(self):
        self.admin_panel.title("Hotel Management System - Admin Panel")

        width = 800
        height = 600
        screen_width = self.admin_panel.winfo_screenwidth()
        screen_height = self.admin_panel.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.admin_panel.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        admin_frame = tk.LabelFrame(self.admin_panel, padx=10, pady=10, font=("Times New Roman", 12))
        admin_frame.grid(row=0, column=0, padx=10, pady=10)

        manage_staff = tk.Button(admin_frame, text="Manage Staff", font=("Times New Roman", 12), command=self.manage_staff_options)
        manage_staff.grid(row=0, column=1, padx=10, pady=10)

        manage_rooms = tk.Button(admin_frame, text="Manage Rooms", font=("Times New Roman", 12), command=self.manage_rooms_options)
        manage_rooms.grid(row=0, column=2, padx=10, pady=10)

        manage_reservations = tk.Button(admin_frame, text="Manage Reservations", font=("Times New Roman", 12), command=self.manage_reservations_options)
        manage_reservations.grid(row=0, column=3, padx=10, pady=10)

        view_logs = tk.Button(admin_frame, text="View Login Logs", font=("Times New Roman", 12), command=self.manage_login_logs)
        view_logs.grid(row=0, column=4, padx=10, pady=10)

        self.admin_panel.mainloop()

    def clear_management_frames(self):
        for widget in self.admin_panel.grid_slaves(row=1, column=0):
            widget.destroy()

    def manage_staff_options(self):
        self.clear_management_frames()
        manage_staff_frame = tk.Frame(self.admin_panel)
        manage_staff_frame.grid(row=1, column=0, columnspan=7, pady=10)

        manage_staff_lframe = tk.LabelFrame(manage_staff_frame, padx=10, pady=0)
        manage_staff_lframe.grid(row=1, column=0, columnspan=7, pady=10)

        add_staff_button = tk.Button(manage_staff_lframe, text="Add Staff", font=("Times New Roman", 12), command=None)
        add_staff_button.grid(row=0, column=0, padx=10, pady=10)

        delete_staff_button = tk.Button(manage_staff_lframe, text="Delete Staff", font=("Times New Roman", 12), command=None)
        delete_staff_button.grid(row=0, column=1, padx=10, pady=10)

        update_staff_button = tk.Button(manage_staff_lframe, text="Update Staff", font=("Times New Roman", 12), command=None)
        update_staff_button.grid(row=0, column=2, padx=10, pady=10)

        view_staff_button = tk.Button(manage_staff_lframe, text="View Staff", font=("Times New Roman", 12), command=None)
        view_staff_button.grid(row=0, column=3, padx=10, pady=10)

    def manage_rooms_options(self):
        self.clear_management_frames()
        manage_rooms_frame = tk.Frame(self.admin_panel)
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

    def manage_reservations_options(self):
        self.clear_management_frames()
        manage_reservations_frame = tk.Frame(self.admin_panel)
        manage_reservations_frame.grid(row=1, column=0, columnspan=7, pady=10)

        manage_reservations_lframe = tk.LabelFrame(manage_reservations_frame, padx=10, pady=10)
        manage_reservations_lframe.grid(row=1, column=0, columnspan=7, pady=10)

        add_reservations_button = tk.Button(manage_reservations_lframe, text="Add Reservations", font=("Times New Roman", 12), command=None)
        add_reservations_button.grid(row=0, column=0, padx=10, pady=10)

        delete_reservations_button = tk.Button(manage_reservations_lframe, text="Delete Reservations", font=("Times New Roman", 12), command=None)
        delete_reservations_button.grid(row=0, column=1, padx=10, pady=10)

        update_reservations_button = tk.Button(manage_reservations_lframe, text="Update Reservations", font=("Times New Roman", 12), command=None)
        update_reservations_button.grid(row=0, column=2, padx=10, pady=10)

    def manage_login_logs(self):
        self.clear_management_frames()
        manage_login_frame = tk.Frame(self.admin_panel)
        manage_login_frame.grid(row=1, column=0, columnspan=7, pady=10)

        manage_login_lframe = tk.LabelFrame(manage_login_frame, padx=10, pady=0)
        manage_login_lframe.grid(row=1, column=0, columnspan=7, pady=10)

        view_login_logs_button = tk.Button(manage_login_lframe, text="View Login Logs", font=("Times New Roman", 12), command=self.view_login_logs)
        view_login_logs_button.grid(row=0, column=0, padx=10, pady=10)

    def view_login_logs(self):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM Log")
        logs = cursor.fetchall()
        cursor.close()
        for log in logs:
            print(log)

class StaffPanel:
    def __init__(self, db):
        self.db = db
        self.staff_panel = tk.Tk()
        self.setup_staff_panel()

    def setup_staff_panel(self):
        self.staff_panel.title("Hotel Management System - Staff Panel")

        width = 800
        height = 600
        screen_width = self.staff_panel.winfo_screenwidth()
        screen_height = self.staff_panel.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.staff_panel.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        staff_frame = tk.LabelFrame(self.staff_panel, padx=10, pady=10, font=("Times New Roman", 12))
        staff_frame.grid(row=0, column=0, padx=10, pady=10)

        manage_rooms = tk.Button(staff_frame, text="Manage Rooms", font=("Times New Roman", 12), command=self.manage_rooms_options)
        manage_rooms.grid(row=0, column=1, padx=10, pady=10)

        manage_reservations = tk.Button(staff_frame, text="Manage Reservations", font=("Times New Roman", 12), command=self.manage_reservations_options)
        manage_reservations.grid(row=0, column=2, padx=10, pady=10)

        self.staff_panel.mainloop()

    def clear_management_frames(self):
        for widget in self.staff_panel.grid_slaves(row=1, column=0):
            widget.destroy()

    def manage_rooms_options(self):
        self.clear_management_frames()
        manage_rooms_frame = tk.Frame(self.staff_panel)
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

    def manage_reservations_options(self):
        self.clear_management_frames()
        manage_reservations_frame = tk.Frame(self.staff_panel)
        manage_reservations_frame.grid(row=1, column=0, columnspan=7, pady=10)

        manage_reservations_lframe = tk.LabelFrame(manage_reservations_frame, padx=10, pady=10)
        manage_reservations_lframe.grid(row=1, column=0, columnspan=7, pady=10)

        add_reservations_button = tk.Button(manage_reservations_lframe, text="Add Reservations", font=("Times New Roman", 12), command=None)
        add_reservations_button.grid(row=0, column=0, padx=10, pady=10)

        delete_reservations_button = tk.Button(manage_reservations_lframe, text="Delete Reservations", font=("Times New Roman", 12), command=None)
        delete_reservations_button.grid(row=0, column=1, padx=10, pady=10)

        update_reservations_button = tk.Button(manage_reservations_lframe, text="Update Reservations", font=("Times New Roman", 12), command=None)
        update_reservations_button.grid(row=0, column=2, padx=10, pady=10)

if __name__ == "__main__":
    db = Database(
        host="localhost",
        user="root",
        password="tarik7172",
        port=3306,
        database="NHMS"
    )

    LoginApp(db)
