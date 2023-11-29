import argparse
import hashlib
import random
import string

def generate_password(lower, upper, digits, special):
    password = ''.join(random.choice(string.ascii_lowercase) for _ in range(lower))
    password += ''.join(random.choice(string.ascii_uppercase) for _ in range(upper))
    password += ''.join(random.choice(string.digits) for _ in range(digits))
    password += ''.join(random.choice(string.punctuation) for _ in range(special))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

def main():
    print("===================================")
    print("  WELCOME TO CYTXV PASSYGEN")
    print("===================================")
    print("""
     _____
    |  __ \\
    | |__) |__  _ __  _ __   ___ _ __
    |  ___/ _ \\| '_ \\| '_ \\ / _ \\ '__|
    | |  | (_) | |_) | |_) |  __/ |
    |_|   \\___/| .__/| .__/ \\___|_|
               | |   | |
               |_|   |_|
    """)
    print("1. Fast Generate")
    print("2. Personalized Generate")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        lower = upper = digits = special = 4  # Predefined configuration for fast generation
    elif choice == 2:
        lower = int(input("Enter the number of lowercase characters: "))
        upper = int(input("Enter the number of uppercase characters: "))
        digits = int(input("Enter the number of digits: "))
        special = int(input("Enter the number of special characters: "))
    else:
        print("[red]Invalid choice![/red]")
        return

    password = generate_password(lower, upper, digits, special)
    hashed_password = hash_password(password)

    print(f"Password: {password}")
    print(f"Hashed Password: {hashed_password}")

if __name__ == "__main__":
    main()