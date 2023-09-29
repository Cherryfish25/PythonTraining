# Math Formula

solvingFor = input("What are you solving for? (D, T, V): ")

if solvingFor == "D":
    T = input("What is the time? ")
    V = input("What is the velocity? ")
    D = V * T
    print("The distance is " + D + ".")

if solvingFor == "T":
    D = input("What is the distance? ")
    V = input("What is the velocity? ")
    T = D / V
    print("The time is " + T + ".")

if solvingFor == "V":
    D = input("What is the distance? ")
    T = input("What is the time? ")
    V = D / T
    print("The velocity is " + V + ".")







