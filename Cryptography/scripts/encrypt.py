import sys
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass

password = getpass()
message = sys.argv[1]

cipher = encrypt(password, message)
encoded_cipher = b64encode(cipher)

print(encoded_cipher)
print("Make sure your replace the b at the beginning and the ' '")
