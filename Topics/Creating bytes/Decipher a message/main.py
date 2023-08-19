# Read the encoded message and the key
encoded_message = input()
key = int(input())

# Convert the key to two bytes and sum up their items
key_bytes = key.to_bytes(2, byteorder='big')
key_sum = sum(key_bytes)

# Initialize an empty string to store the decoded message
decoded_message = ''

# Iterate through each character in the encoded message
for char in encoded_message:
    # Calculate the new code point by adding the key sum
    new_code = ord(char) + key_sum

    # Convert the new code point back to a character and append it to the decoded message
    decoded_message += chr(new_code)

# Print the decoded message
print(decoded_message)