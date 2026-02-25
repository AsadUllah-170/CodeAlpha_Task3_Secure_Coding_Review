# secure_login_system.py
# Secure Python login system with password hashing

import hashlib

# Store hashed passwords
users = {
    "admin": hashlib.sha256("12345".encode()).hexdigest(),
    "user1": hashlib.sha256("password".encode()).hexdigest()
}

def login(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed:
        print("Login successful!")
    else:
        print("Login failed!")

# User input
username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)
