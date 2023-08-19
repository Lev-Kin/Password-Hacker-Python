# Open the input file for reading
with open("animals.txt", "r") as input_file:
    # Read the lines and remove '\n' using rstrip
    animals_list = [line.rstrip() for line in input_file]

# Open the output file for writing
with open("animals_new.txt", "w") as output_file:
    # Write the animals separated by a whitespace
    output_file.write(" ".join(animals_list))