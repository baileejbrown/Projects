"""Bailee Brown"""

MIN_LENGTH = 6


def main():
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Please enter a password 6 digits or longer: ")
    while len(password) < MIN_LENGTH:
        print("Password not long enough,")
        password = input("Please enter a valid password: ")
    return password


main()
