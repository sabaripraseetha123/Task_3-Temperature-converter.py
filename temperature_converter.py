def convert_temperature():
    temp = float(input("Enter temperature: "))
    unit = input("Convert to (C/F/K): ").upper()

    if unit == 'C':
        celsius = (temp - 32) * 5/9
        print(f"{temp}F = {celsius:.2f}C")
    elif unit == 'F':
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}C = {fahrenheit:.2f}F")
    elif unit == 'K':
        kelvin = temp + 273.15
        print(f"{temp}C = {kelvin:.2f}K")
    else:
        print("Invalid unit")

convert_temperature()