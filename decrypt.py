import cv2
import struct
import hashlib

# Read the encrypted image
img = cv2.imread("encryptedImage.png")
assert img is not None, "Encrypted image not found!"

# User input for password
user_password = input("Enter passcode for decryption: ")

n, m, z = 0, 0, 0  # start at first pixel
height, width, _ = img.shape

# Extract stored password hash (first 32 bytes)
stored_hash = bytes([img[n + i, m + i, (i % 3)] for i in range(32)])

# Compute hash of user's input
input_hash = hashlib.sha256(user_password.encode()).digest()

# Validate password
if stored_hash != input_hash:
    print("Incorrect password!")
    exit()

# Move to the message metadata (after 32-byte hash)
n, m, z = 32, 32, (32 % 3)

# Extract message length (next 4 bytes)
msg_length_bytes = bytes([img[n + i, m + i, (z + i) % 3] for i in range(4)])
msg_length = struct.unpack(">I", msg_length_bytes)[0]

# Move to the message data (after hash + 4-byte length)
n, m, z = 36, 36, (36 % 3)

# Extract the message
message = []
for i in range(msg_length):
    message.append(img[n + i, m + i, (z + i) % 3])
message = bytes(message).decode()

print("Decrypted message:", message)