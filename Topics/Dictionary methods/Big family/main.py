def new_family(first_family, second_family):

    new_family = first_family.copy()
    new_family.update(second_family)

    return new_family


# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

# Create a new dictionary
new_family = new_family(first_family, second_family)

# Print the new dictionary
print(new_family)