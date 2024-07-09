import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

# Database connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tarik7172',
    'port': 3306,
    'database': 'NHMS'
}

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.connection = mysql.connector.connect(**db_config)
        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()
        self.login_frame = tk.Frame(self.root)
        self.login_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(self.login_frame, text="Hotel Management System", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.login_frame, text="Username", font=("Arial", 14)).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.login_frame, text="Password", font=("Arial", 14)).grid(row=2, column=0, padx=5, pady=5)

        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 14))
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show='*', font=("Arial", 14))
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.login_frame, text="Login", command=self.login, font=("Arial", 14)).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM Users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            self.log_login(user['user_id'])
            if user['role'] == 'admin':
                self.create_admin_panel(user)
            else:
                self.create_staff_panel(user)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def log_login(self, user_id):
        cursor = self.connection.cursor()
        query = "INSERT INTO Log (user_id, login_time) VALUES (%s, %s)"
        cursor.execute(query, (user_id, datetime.now()))
        self.connection.commit()
        cursor.close()

    def create_admin_panel(self, user):
        self.clear_frame()
        self.create_navbar(user, is_admin=True)
        self.create_content_frame()
        self.show_welcome_message(user)

    def create_staff_panel(self, user):
        self.clear_frame()
        self.create_navbar(user, is_admin=False)
        self.create_content_frame()
        self.show_welcome_message(user)

    def create_navbar(self, user, is_admin):
        self.nav_frame = tk.Frame(self.root, bg="lightgrey")
        self.nav_frame.grid(row=0, column=0, rowspan=2, sticky='ns')
        
        user_info = f"Welcome {user['name']} {user['surname']}\nRole: {user['role']}"
        tk.Label(self.nav_frame, text=user_info, font=("Arial", 14), bg="lightgrey").pack(pady=10)

        buttons = []
        if is_admin:
            buttons = [
                ("View Login Logs", self.view_login_logs),
                ("Manage Users", self.dummy_function),
                ("Manage Rooms", self.dummy_function),
                ("Manage Guests", self.dummy_function),
                ("Manage Reservations", self.dummy_function),
                ("Manage Billing", self.dummy_function),
                ("Manage Charges", self.dummy_function),
                ("Manage Maintenance Requests", self.dummy_function),
                ("Manage Housekeeping", self.dummy_function),
                ("Manage Amenities", self.dummy_function),
                ("Manage Feedback", self.dummy_function),
                ("Manage Inventory", self.dummy_function),
                ("Manage Events", self.dummy_function),
            ]
        else:
            buttons = [
                ("View Reservations", self.dummy_function),
                ("Update Room Status", self.dummy_function),
                ("View Guests", self.dummy_function),
                ("View Billing", self.dummy_function),
                ("View Charges", self.dummy_function),
                ("View Maintenance Requests", self.dummy_function),
                ("Update Housekeeping", self.dummy_function),
                ("View Amenities", self.dummy_function),
                ("View Feedback", self.dummy_function),
                ("View Inventory", self.dummy_function),
                ("View Events", self.dummy_function),
            ]

        for text, command in buttons:
            tk.Button(self.nav_frame, text=text, command=command, font=("Arial", 12), width=25).pack(pady=2)

        tk.Button(self.nav_frame, text="Logout", command=self.create_login_frame, font=("Arial", 12), width=25).pack(pady=20)

    def create_content_frame(self):
        self.content_frame = tk.Frame(self.root)
        self.content_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

    def show_welcome_message(self, user):
        welcome_message = f"Welcome to the Hotel Management System, {user['name']} {user['surname']}!"
        tk.Label(self.content_frame, text=welcome_message, font=("Arial", 18)).pack(pady=20)

    def view_login_logs(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Login Logs", font=("Arial", 18)).pack(pady=10)

        columns = ('log_id', 'username', 'name', 'surname', 'position', 'role', 'login_time')
        tree = ttk.Treeview(self.content_frame, columns=columns, show='headings')
        tree.pack(fill=tk.BOTH, expand=True)

        tree.heading('log_id', text='Log ID')
        tree.heading('username', text='Username')
        tree.heading('name', text='Name')
        tree.heading('surname', text='Surname')
        tree.heading('position', text='Position')
        tree.heading('role', text='Role')
        tree.heading('login_time', text='Login Time')

        tree.column('log_id', width=50)
        tree.column('username', width=100)
        tree.column('name', width=100)
        tree.column('surname', width=100)
        tree.column('position', width=100)
        tree.column('role', width=100)
        tree.column('login_time', width=150)

        scrollbar = ttk.Scrollbar(self.content_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        cursor = self.connection.cursor(dictionary=True)
        query = """
        SELECT Log.log_id, Users.username, Users.name, Users.surname, Users.position, Users.role, Log.login_time 
        FROM Log 
        JOIN Users ON Log.user_id = Users.user_id 
        ORDER BY Log.login_time DESC
        """
        cursor.execute(query)
        logs = cursor.fetchall()
        cursor.close()

        for log in logs:
            tree.insert('', tk.END, values=(log['log_id'], log['username'], log['name'], log['surname'], log['position'], log['role'], log['login_time']))

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def dummy_function(self):
        messagebox.showinfo("Info", "This functionality is not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
