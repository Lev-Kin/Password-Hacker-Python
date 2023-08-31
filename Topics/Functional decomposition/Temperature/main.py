def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    temperature = float(temperature)  # convert temperature to a float

    if unit.lower() == 'c':
        converted_temp = celsius_to_fahrenheit(temperature)
        new_unit = 'F'
    elif unit.lower() == 'f':
        converted_temp = fahrenheit_to_celsius(temperature)
        new_unit = 'C'
    else:
        print("Invalid unit")
        return

    print(f"{converted_temp} {new_unit}")



