import hashlib
import random
import string

def generate_password(lower, upper, digits, special):
    # Generate a random password
    password = ''.join(random.choice(string.ascii_lowercase) for _ in range(lower))
    password += ''.join(random.choice(string.ascii_uppercase) for _ in range(upper))
    password += ''.join(random.choice(string.digits) for _ in range(digits))
    password += ''.join(random.choice(string.punctuation) for _ in range(special))

    # Convert the password into a list and shuffle it
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def hash_password(password):
    # Hash the password using SHA256
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

# Ask the user to specify the number of each type of character
lower = int(input("Enter the number of lowercase characters: "))
upper = int(input("Enter the number of uppercase characters: "))
digits = int(input("Enter the number of digits: "))
special = int(input("Enter the number of special characters: "))

password = generate_password(lower, upper, digits, special)
hashed_password = hash_password(password)

print(f"Password: {password}")
print(f"Hashed Password: {hashed_password}")
