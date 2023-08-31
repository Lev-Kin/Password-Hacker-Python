def caesar_cipher(text):
    encrypted_text = ""

    for char in text:
        encrypted_text += chr(ord(char) + 1)

    return encrypted_text

# Read input string
text = input()

# Encrypt the input string
encrypted_text = caesar_cipher(text)

# Print the encrypted string
print(encrypted_text)