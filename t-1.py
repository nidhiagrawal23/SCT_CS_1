def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        result = caesar_encrypt(text, shift)
        print(f"Encrypted text: {result}")
    elif choice == 'd':
        result = caesar_decrypt(text, shift)
        print(f"Decrypted text: {result}")
    else:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
