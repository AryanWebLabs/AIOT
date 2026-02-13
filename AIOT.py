import os
import time
import random
import string
import hashlib
from colorama import Fore, Style, init
import readchar  # pip install readchar

init(autoreset=True)

# Clear terminal
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# Banner
def banner():
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    print(Fore.MAGENTA + Style.BRIGHT + "         Aryan's HighTech Security Toolkit 🚀")
    print(Fore.CYAN + Style.BRIGHT + "="*60 + "\n")

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
        print(Fore.RED + "Weak ❌")
    elif score <= 4:
        print(Fore.YELLOW + "Medium ⚠️")
    else:
        print(Fore.GREEN + "Strong ✅")
    input("\nPress Enter to return to menu...")

# 2. Password Generator
def password_generator():
    clear()
    banner()
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print(Fore.GREEN + f"Generated Password: {pwd}")
    input("\nPress Enter to return to menu...")

# 3. Hash Generator
def hash_generator():
    clear()
    banner()
    data = input("Enter text or password to hash: ")
    print(Fore.YELLOW + "\nSelect Hash Type:")
    print("1. MD5\n2. SHA1\n3. SHA256")
    choice = input("Choice: ")
    if choice == "1":
        hashed = hashlib.md5(data.encode()).hexdigest()
    elif choice == "2":
        hashed = hashlib.sha1(data.encode()).hexdigest()
    elif choice == "3":
        hashed = hashlib.sha256(data.encode()).hexdigest()
    else:
        print(Fore.RED + "Invalid choice!")
        time.sleep(1)
        return
    print(Fore.GREEN + f"Hashed Value: {hashed}")
    input("\nPress Enter to return to menu...")

# 4. Random Key / Token Generator
def token_generator():
    clear()
    banner()
    length = int(input("Enter token length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+=<>?"
    token = ''.join(random.choice(chars) for _ in range(length))
    print(Fore.GREEN + f"Generated Token: {token}")
    input("\nPress Enter to return to menu...")

# ---------------- Menu ----------------
tools = ["Password Checker", "Password Generator", "Hash Generator", "Token Generator", "Exit"]

def main_menu():
    idx = 0
    while True:
        clear()
        banner()
        print(Fore.CYAN + "Use UP/DOWN arrows to navigate and Enter to select:\n")
        for i, tool in enumerate(tools):
            if i == idx:
                print(Fore.MAGENTA + ">> " + tool)
            else:
                print("   " + tool)

        key = readchar.readkey()
        if key == readchar.key.UP:
            idx = (idx - 1) % len(tools)
        elif key == readchar.key.DOWN:
            idx = (idx + 1) % len(tools)
        elif key == readchar.key.ENTER:
            if tools[idx] == "Password Checker":
                password_checker()
            elif tools[idx] == "Password Generator":
                password_generator()
            elif tools[idx] == "Hash Generator":
                hash_generator()
            elif tools[idx] == "Token Generator":
                token_generator()
            elif tools[idx] == "Exit":
                print(Fore.MAGENTA + "Exiting... Bye 👋")
                time.sleep(1)
                break

if __name__ == "__main__":
    main_menu()
