# login_system.py
# Simple Python login system (vulnerable version)

users = {"admin": "12345", "user1": "password"}

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed!")

# User input
username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)
