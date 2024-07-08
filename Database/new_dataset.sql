

-- Insert an admin user
INSERT INTO Users (name,surname,position, role, username, password, phone, address)
VALUES ('Admin',"Adminoğlu","Admin" ,'admin', 'admin', 'a', '1234567890', '123 Admin Street, Admin City');

-- Insert a staff user
INSERT INTO Users (name,surname,position, role, username, password, phone, address)
VALUES ('Staff User', "Staffoğlu","Staff" ,'staff', 'staff', 's', '0987654321', '456 Staff Avenue, Staff City');
