import os
import random
import string
import hashlib
import time

# ---------------- Helper ----------------
def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("="*60)
    print(" " * 10 + "🔥🔥🔥 ARYAN'S HIGH-TECH TOOLKIT 🔥🔥🔥")
    print("="*60 + "\n")

# ---------------- Tools ----------------

# 1. Password Checker
def password_checker():
    clear()
    banner()
    password = input("Enter password to check: ")
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*(),.?\":{}|<>" for c in password): score += 1

    if score <= 2:
        print("\nPassword Strength: Weak ❌")
    elif score <= 4:
        print("\nPassword Strength: Medium ⚠️")
    else:
        print("\nPassword Strength: Strong ✅")
    input("\nPress Enter to return to menu...")

# 2. Password Generator
def password_generator():
    clear()
    banner()
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print(f"\nGenerated Password: {pwd}")
    input("\nPress Enter to return to menu...")

# 3. Hash Generator
def hash_generator():
    clear()
    banner()
    data = input("Enter text/password to hash: ")
    print("\nSelect Hash Type:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    choice = input("Choice: ")
    if choice == "1":
        hashed = hashlib.md5(data.encode()).hexdigest()
    elif choice == "2":
        hashed = hashlib.sha1(data.encode()).hexdigest()
    elif choice == "3":
        hashed = hashlib.sha256(data.encode()).hexdigest()
    else:
        print("\nInvalid choice!")
        time.sleep(1)
        return
    print(f"\nHashed Value: {hashed}")
    input("\nPress Enter to return to menu...")

# 4. Random Token Generator
def token_generator():
    clear()
    banner()
    length = int(input("Enter token length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+=<>?"
    token = ''.join(random.choice(chars) for _ in range(length))
    print(f"\nGenerated Token: {token}")
    input("\nPress Enter to return to menu...")

# ---------------- Main Menu ----------------
def main_menu():
    while True:
        clear()
        banner()
        print("1. Password Checker")
        print("2. Password Generator")
        print("3. Hash Generator")
        print("4. Token Generator")
        print("5. Exit\n")
        choice = input("Select an option [1-5]: ")

        if choice == "1":
            password_checker()
        elif choice == "2":
            password_generator()
        elif choice == "3":
            hash_generator()
        elif choice == "4":
            token_generator()
        elif choice == "5":
            print("\nExiting... Bye 👋")
            time.sleep(1)
            break
        else:
            print("\nInvalid Option! Try again.")
            time.sleep(1)

# ---------------- Run ----------------
if __name__ == "__main__":
    main_menu()
