# MY-PROJECT--passwordgenerator.py
This project is a Python-based password generator that asks a few simple questions and creates a strong, memorable password. It is designed for users who want both security and personalization in their passwords.

import random
import string

def generate_password():
    fav_color = input("What is your favorite color? ").strip()
    pet_name = input("What is your pet’s name (or favorite animal)? ").strip()
    birth_year = input("What is your birth year? ").strip()

    base = fav_color[:3].capitalize() + pet_name[-3:].capitalize() + birth_year[-2:]

    special_chars = "!@#$%^&*?"
    random_part = ''.join(random.choice(string.ascii_letters + string.digits + special_chars) for _ in range(4))

    password = base + random_part
    return password

print("Your generated password is:", generate_password())
