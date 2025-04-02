import cv2
import os
import struct
import hashlib

# Read the image
img = cv2.imread("horses.jpg")  # Image Path
assert img is not None, "Image not found!"

# User inputs
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Generate password hash (SHA-256)
password_hash = hashlib.sha256(password.encode()).digest()  # 32-byte hash

# Prepare message metadata
msg_bytes = msg.encode()
msg_length = struct.pack(">I", len(msg_bytes))  # 4-byte message length

# Combine all data: hash + msg_length + msg
data = password_hash + msg_length + msg_bytes

# Check if image can hold the data
required_pixels = len(data)
height, width, _ = img.shape
if required_pixels > height * width:
    print("Image too small to hide data!")
    exit()

# Embed data into image
n, m, z = 0, 0, 0
for byte in data:
    img[n, m, z] = byte
    n += 1
    m += 1
    z = (z + 1) % 3

# Save and open the encrypted image
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  
