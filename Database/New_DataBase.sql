-- Create the database
CREATE DATABASE HMS;
USE HMS;

-- Rooms Table
CREATE TABLE Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    UNIQUE (room_number)
);

-- Guests Table
CREATE TABLE Guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    preferences TEXT,
    past_stays TEXT
);

-- Reservations Table
CREATE TABLE Reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    guest_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    INDEX (room_id),
    INDEX (guest_id)
);

-- Billing Table
CREATE TABLE Billing (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    bill_contents TEXT NOT NULL,
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    INDEX (guest_id)
);

-- Users Table (including username and hashed password)
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role ENUM('admin', 'staff') NOT NULL,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    CHECK (role IN ('admin', 'staff'))
);

-- Log Table (for tracking login/logout events)
CREATE TABLE Log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    login_time DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    INDEX (user_id)
);

-- Charges Table (for itemized billing)
CREATE TABLE Charges (
    charge_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT NOT NULL,
    description TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    charge_date DATETIME NOT NULL,
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    INDEX (guest_id)
);

-- MaintenanceRequests Table
CREATE TABLE MaintenanceRequests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    issue_description TEXT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    request_date DATETIME NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    INDEX (room_id),
    INDEX (user_id)
);
