-- Create the database
CREATE DATABASE IF NOT EXISTS HotelManagementSystem;
USE HotelManagementSystem;

-- Rooms Table
CREATE TABLE Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number INT,
    type VARCHAR(50),
    status VARCHAR(50)
);

ALTER TABLE Rooms ADD CONSTRAINT unique_room_number UNIQUE (room_number);


-- Guests Table
CREATE TABLE Guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(255),
    preferences TEXT,
    past_stays TEXT
);

-- Reservations Table
CREATE TABLE Reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT,
    guest_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id)
);

-- Billing Table
CREATE TABLE Billing (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT,
    amount DECIMAL(10, 2),
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
);

-- Staff Table (including username and password)
CREATE TABLE Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(100)
);

-- Admin Table (including name, username, and password)
CREATE TABLE Admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(100)
);

-- Log Table (for tracking login/logout events)
CREATE TABLE Log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(255) NOT NULL,
    user_type ENUM('admin', 'staff'),
    login_time DATETIME
);

-- Charges Table (for itemized billing)
CREATE TABLE Charges (
    charge_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT,
    description VARCHAR(255),
    amount DECIMAL(10, 2),
    charge_date DATETIME,
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
);

CREATE TABLE MaintenanceRequests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number INT NOT NULL,
    issue_description TEXT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_number) REFERENCES Rooms(room_number)
);

