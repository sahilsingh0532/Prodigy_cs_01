def encrypt(text, s):
    result = ""

    for char in text:
        if char.isupper():  
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():  
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char  

    return result

def decrypt(text, s):
    result = ""

    for char in text:
        if char.isupper():  
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():  
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char  

    return result

choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
text = input("Enter the message: ")
s = int(input("Enter the shift value: "))

if choice == 'e':
    print("\nEncrypted Text:", encrypt(text, s))
elif choice == 'd':
    print("\nDecrypted Text:", decrypt(text, s))
else:
    print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")
