# Steganography-Project-Using-Python


A Python tool for hiding secret messages inside images using steganography with password protection.

## Features

-  Encrypt text messages into images with AES-256 password protection
-  Decrypt hidden messages using the correct password
-  Uses lossless PNG format to preserve data integrity
-  Secure SHA-256 password hashing
-  Automatic size validation for carrier images

## Usage
### Encryption : 
-- **python** encrypt.py

- Enter secret message or text file path
- Set a password
- Input image: horses.jpg (default) or your own
- Output: encryptedImage.png


### Decryption : 
-- **python** decrypt.py

- Provide encrypted image (encryptedImage.png)
- Enter password
- Output: Decrypted message to console


# How It Works
## Encryption Process

- Password converted to SHA-256 hash
- Text message converted to binary
- Data embedded in image pixels using LSB substitution
- Metadata (password hash, message length) stored in first 36 pixels

## Decryption Process

- Extract password hash from image
- Validate user password against stored hash
- Extract message length and content
- Save decrypted message

# File Structure

- encrypt.py           # Encryption script
- decrypt.py           # Decryption script
- horses.jpg           # Sample carrier image
- requirements.txt     # Dependencies
- README.md            # This documentation


## License
Open Source
