# Read the input string
input_string = input()

# Convert the string to a bytes object
bytes_object = bytes(input_string, encoding='utf-8')

# Output the last item of the bytes object
print(bytes_object[-1])
