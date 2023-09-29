print("Welcome to the 100 years old calculator")
Age = input("How old are you? ")
CurrentYear = input("What year is it currently? ")
Until100 = 100 - int(Age)
Year100 = int(CurrentYear) + Until100
print("In " + str(Until100) + " years, in the year " + str(Year100) + ", you will be 100 years old.")
