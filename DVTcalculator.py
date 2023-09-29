# DVT Calculator

distanceType = "blank"
timeType = "blank"

def timeTypeFunction(VM):
    global timeType
    if VM == "km/h":
        timeType = "hours"
    elif VM == "mph":
        timeType = "hours"
    elif VM == "m/s":
        timeType = "seconds"
    elif VM == "f/m":
        timeType = "minutes"
    elif VM == "in/s":
        timeType = "seconds"
    elif VM == "cm/s":
        timeType = "seconds"
    else:
        timeType = " *! Invalid measurement !* "
        print("Restart program and enter a valid measurement. ")

def distanceTypeFunction(VM):
    global distanceType
    if VM == "km/h":
        distanceType = "kilometers"
    elif VM == "mph":
        distanceType = "miles"
    elif VM == "m/s":
        distanceType = "meters"
    elif VM == "f/m":
        distanceType = "feet"
    elif VM == "in/s":
        distanceType = "inches"
    elif VM == "cm/s":
        distanceType = "centimeters"
    else:
        distanceType = " *! Invalid measurement !* "
        print("Restart program and enter a valid measurement. ")

target = False

while target == False:
    solvingFor = input("What are you solving for? ")
    if (solvingFor == "D") or (solvingFor == "V") or (solvingFor == "T"):
        target = True
    else:
        print("That is not a valid answer. ")

if solvingFor == "D":
    vMeasurement = input("Is the velocity in km/h, mph, m/s, f/m, in/s, or cm/s? ")
    timeTypeFunction(vMeasurement)
    T = input("What is the time in " + timeType + "? ")
    V = input("What is the velocity in " + vMeasurement + "? ")
    D = int(V) * int(T)
    if vMeasurement == "km/h":
        print("The distance is " + str(D) + " kilometers.")
    elif vMeasurement == "mph":
        print("The distance is " + str(D) + " miles.")
    elif vMeasurement == "m/s":
        print("The distance is " + str(D) + " meters.")
    elif vMeasurement == "f/m":
        print("The distance is " + str(D) + " feet.")
    elif vMeasurement == "in/s":
        print("The distance is " + str(D) + " inches.")
    elif vMeasurement == "cm/s":
        print("The distance is " + str(D) + " centimeters.")

if solvingFor == "V":
    vMeasurement = input("Is the velocity in: km/h, mph, m/s, f/m, in/s, or cm/s? ")
    distanceTypeFunction(vMeasurement)
    timeTypeFunction(vMeasurement)
    D = input("What is the distance in " + distanceType + "? ")
    T = input("What is the time in " + timeType + "? ")
    V = int(D) / int(T)
    if distanceType == "kilometers":
        print("The velocity is " + str(V) + " km/h.")
    elif distanceType == "miles":
        print("The velocity is " + str(V) + " mph.")
    elif distanceType == "meters":
        print("The velocity is " + str(V) + " m/s.")
    elif distanceType == "feet":
        print("The velocity is " + str(V) + " f/m.")
    elif distanceType == "inches":
        print("The velocity is " + str(V) + " in/s.")
    elif distanceType == "centimeters":
        print("The velocity is " + str(V) + " cm/s.")
    else:
        print("This is an invalid measurement!! ")

if solvingFor == "T":
    vMeasurement = input("Is the velocity in: km/h, mph, m/s, f/m, in/s, or cm/s? ")
    distanceTypeFunction(vMeasurement)
    D = input("What is the distance in " + distanceType + "? ")
    V = input("What is the velocity in " + vMeasurement + "? ")
    T = int(D) / int(V)
    if vMeasurement == "km/h":
        print("The time is " + str(T) + " hours.")
    elif vMeasurement == "mph":
        print("The time is " + str(T) + " hours.")
    elif vMeasurement == "m/s":
        print("The time is " + str(T) + " seconds.")
    elif vMeasurement == "f/m":
        print("The time is " + str(T) + " minutes.")
    elif vMeasurement == "in/s":
        print("The time is " + str(T) + " seconds.")
    elif vMeasurement == "cm/s":
        print("The time is " + str(T) + " seconds.")
    else:
        print("That is an invalid measurement, bruh. ")
