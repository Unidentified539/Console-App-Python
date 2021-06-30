import os
from cryptography.fernet import Fernet


def menu():
    choices = str(input("""
                Application Menu
    1. Type one to decrypt a file.
    2. Type two to encrypt a file.
    3. Type three to encrypt text from terminal
    4. Type four to decrypt text from terminal.
    5. Type five to exit.
    6. Type six to see command center.            
    """))
    if choices == "1":
        choice_1()
    if choices == "2":
        choice_2()
    if choices == "3":
        choice_3()
    if choices == "4":
        choice_4()
    if choices == "5":
        print("Goodbye")


def choice_1():
    key_path = str(input("Enter key path: "))
    file_path = str(input("Enter file path: "))
    decrypt(file_path, key_path)
    menu()


def choice_2():
    key_path = str(input("Enter path for key to: "))
    file_path = str(input("Enter file path: "))
    generate_key(key_path)
    encrypt(file_path, key_path)
    menu()


def choice_3():
    text = str(input("Enter text to encrypt: "))
    os.system("cd scripts && python3 encrypt.py \"" + text + "\"")
    menu()


def choice_4():
    text0 = str(input("Enter text to decrypt: "))
    os.system("cd scripts && python3 decrypt.py \"" + text0 + "\"")
    menu()


# Encryption

def generate_key(filepath_to_generate_key):
    # key generation
    key = Fernet.generate_key()
    # string the key in a file
    with open(filepath_to_generate_key, 'wb') as filekey:
        filekey.write(key)


def encrypt(file_path, key_path):
    # opening the key
    with open(key_path, 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(file_path, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt(file_path, key_path):
    # opening the key
    with open(key_path, 'rb') as filekey:
        key = filekey.read()

    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open(file_path, 'wb') as dec_file:
        dec_file.write(decrypted)

menu()
