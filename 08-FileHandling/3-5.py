import re

# Read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# Pattern (criteria) for username: At least 6 characters, lowercase letters only
username_pattern = r'^[a-z]{6,}$'

# Pattern (criteria) for password: At least 8 characters, letters, numbers, and underscores
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

# Check if username and password are valid
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# Print results
if username_match and password_match:
    print("Username and password are valid.")
else:
    if not username_match:
        print("Invalid username: It must be at least 6 characters long and contain only lowercase letters.")
    if not password_match:
        print("Invalid password: It must be at least 8 characters long and contain only letters, numbers, and underscores.")
