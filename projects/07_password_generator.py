import random
import string


password_length = int(input("Enter password length: "))
passwordcount = int(input("How many passwords do you want? "))


characters = string.ascii_letters + string.digits + string.punctuation

# Generate passwords
for _ in range(passwordcount):
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(password)
