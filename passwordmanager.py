import random
import string
import json
import os


DATA_FILE = "passwords.json"


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def save_password(website, username, password):
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    data[website] = {"username": username, "password": password}

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f" Password saved for {website}!")

def get_password(website):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if website in data:
                return data[website]
    return None


def main():
    while True:
        print("\n===  Python Password Manager ===")
        print("1. Generate a new password")
        print("2. Save a password")
        print("3. Retrieve a password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length (default 12): ") or 12)
            print("Generated Password:", generate_password(length))

        elif choice == "2":
            website = input("Enter website/app name: ")
            username = input("Enter username/email: ")
            password = input("Enter password (leave blank to auto-generate): ")
            if not password:
                password = generate_password()
                print("Generated Password:", password)
            save_password(website, username, password)

        elif choice == "3":
            website = input("Enter website/app name: ")
            result = get_password(website)
            if result:
                print(f" Username: {result['username']} | Password: {result['password']}")
            else:
                print(" No password found for that website.")

        elif choice == "4":
            print(" Exiting Password Manager. Stay secure!")
            break
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    main()
