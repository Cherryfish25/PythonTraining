# Temperature Functions

def CelsiusOrFahrenheit():

    Measurement = input("Would you like to know the temperature in celsius or fahrenheit? (C/F) ")

    if Measurement == "F":
        result = FahrenheitToCelsius()
        print(result)

    elif Measurement == "C":
        result = CelsiusToFahrenheit()
        print(result)

    else:
        print("That is an invalid measurement. Restart program and enter a valid measurement. ")

def CelsiusToFahrenheit():
    Celsius = int(input("Enter the temperature in celsius. "))
    temp = (Celsius * 9/5) + 32
    return temp

def FahrenheitToCelsius():
    Fahrenheit = int(input("Enter the temperature in fahrenheit. "))
    temp = (Fahrenheit - 32) * 5/9
    return temp

CelsiusOrFahrenheit()
