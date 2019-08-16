"""Bailee Brown"""

MIN_LENGTH = 6

password = input("Please enter a password 6 digits or longer: ")

while len(password) < MIN_LENGTH:
    print("Password not long enough,")
    password = input("Please enter a valid password: ")

print(len(password)*'*')