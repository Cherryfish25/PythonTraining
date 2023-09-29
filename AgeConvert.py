# Age Convert

age = input("How many years old are you? ")

days = int(age) * 365

minutes = int(days) * 1440

seconds = int(minutes) * 60

print("You are " + str(days) + " days, " + str(minutes) + " minutes, and " + str(seconds) + " seconds old. ")


