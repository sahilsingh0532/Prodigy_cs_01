﻿# Prodigy_cs_01

## Task Overview
This project implements a **Caesar Cipher** encryption and decryption program in Python. The program allows users to input a message and a shift value to perform both encryption and decryption.

## How It Works
The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

### Formula:
- Encryption: `CipherText = (PlainText + Shift) % 26`
- Decryption: `PlainText = (CipherText - Shift) % 26`

## Features
- Encrypts a given text using the Caesar Cipher algorithm.
- Decrypts a given cipher text back to the original message.
- Allows users to input a message and specify the shift value.

## Installation & Setup
Ensure you have Python installed on your system. If not, download and install it from [Python Official Website](https://www.python.org/downloads/).

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/caesar-cipher.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Prodigy_cs_01
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Usage
1. Run the program.
2. Enter a message to encrypt.
3. Enter the shift value (an integer).
4. View the encrypted text.
5. Enter the encrypted text and shift value to decrypt it back.

## Example
```
Enter the message: HELLO
Enter shift value: 3
Encrypted Message: KHOOR

Enter the encrypted message: KHOOR
Enter shift value: 3
Decrypted Message: HELLO
```


## Contributing
Feel free to fork this repository and submit pull requests to enhance the project.

## License
This project is licensed under the MIT License.

---
