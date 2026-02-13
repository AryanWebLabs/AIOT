import os
import random
import string
import hashlib
import time

# ---------------- Helper Functions ----------------
def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("="*60)
    print(" " * 20 + "ARYAN")
    print("="*60 + "\n")

def pause():
    input("\nPress Enter to return to menu...")

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
    pause()

# 2. Password Generator
def password_generator():
    clear()
    banner()
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print(f"\nGenerated Password: {pwd}")
    pause()

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
        pause()
        return
    print(f"\nHashed Value: {hashed}")
    pause()

# 4. Random Token Generator
def token_generator():
    clear()
    banner()
    length = int(input("Enter token length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+=<>?"
    token = ''.join(random.choice(chars) for _ in range(length))
    print(f"\nGenerated Token: {token}")
    pause()

# 5. Simple Caesar Cipher Encrypt
def caesar_encrypt():
    clear()
    banner()
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift number (e.g., 3): "))
    encrypted = "".join(
        chr((ord(c) - 32 + shift) % 95 + 32) if 32 <= ord(c) <= 126 else c
        for c in text
    )
    print(f"\nEncrypted Text: {encrypted}")
    pause()

# 6. Simple Caesar Cipher Decrypt
def caesar_decrypt():
    clear()
    banner()
    text = input("Enter text to decrypt: ")
    shift = int(input("Enter shift number (e.g., 3): "))
    decrypted = "".join(
        chr((ord(c) - 32 - shift) % 95 + 32) if 32 <= ord(c) <= 126 else c
        for c in text
    )
    print(f"\nDecrypted Text: {decrypted}")
    pause()

# 7. Random Username Generator
def username_generator():
    clear()
    banner()
    length = int(input("Enter username length: "))
    chars = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(chars) for _ in range(length))
    print(f"\nGenerated Username: {username}")
    pause()

# 8. Random Number Generator
def number_generator():
    clear()
    banner()
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
    randnum = random.randint(start, end)
    print(f"\nRandom Number: {randnum}")
    pause()

# 9. Simple Dice Roller
def dice_roller():
    clear()
    banner()
    sides = int(input("Enter number of sides on dice: "))
    roll = random.randint(1, sides)
    print(f"\nYou rolled: {roll}")
    pause()

# 10. Coin Flip Simulator
def coin_flip():
    clear()
    banner()
    flip = random.choice(["Heads", "Tails"])
    print(f"\nCoin Result: {flip}")
    pause()

# ---------------- Main Menu ----------------
def main_menu():
    while True:
        clear()
        banner()
        print("1. Password Checker")
        print("2. Password Generator")
        print("3. Hash Generator")
        print("4. Token Generator")
        print("5. Caesar Cipher Encrypt")
        print("6. Caesar Cipher Decrypt")
        print("7. Random Username Generator")
        print("8. Random Number Generator")
        print("9. Dice Roller")
        print("10. Coin Flip")
        print("11. Exit\n")
        choice = input("Select an option [1-11]: ")

        if choice == "1": password_checker()
        elif choice == "2": password_generator()
        elif choice == "3": hash_generator()
        elif choice == "4": token_generator()
        elif choice == "5": caesar_encrypt()
        elif choice == "6": caesar_decrypt()
        elif choice == "7": username_generator()
        elif choice == "8": number_generator()
        elif choice == "9": dice_roller()
        elif choice == "10": coin_flip()
        elif choice == "11":
            print("\nExiting... Bye 👋")
            time.sleep(1)
            break
        else:
            print("\nInvalid Option! Try again.")
            time.sleep(1)

# ---------------- Run ----------------
if __name__ == "__main__":
    main_menu()

# ---------------- Run ----------------
if __name__ == "__main__":
    main_menu()

