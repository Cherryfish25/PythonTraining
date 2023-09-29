# Age Convert 2

from datetime import date

# Get today's date
today = date.today()

# Separate year, month, and day
year = today.year

month = today.month

day = today.day

# User inputs their birth info
# Must be numerical!!
birthYear = input("What is your birth year? ")

birthMonth = input("What is your birth month? ")

birthDay = input("What is your birth day? ")

# Creating variables to use later
userMonths = 0

userDays = 0

# Create functions for months and days old
def monthFunction():
    if month > int(birthMonth):
        global userMonths
        userMonths = month - int(birthMonth)

    else:
        global userYears
        userMonths = (int(birthMonth) - 1) + (12 - (month + 1))
        userYears -= 1


def dayFunction():
    if day > int(birthDay):
        global userDays
        userDays = day - int(birthDay)

    else:
        userDays = (int(birthDay) - 1) + (30 - (day + 1))

# Do the math and run the functions
userYears = year - int(birthYear)

monthFunction()

dayFunction()

# Print the final age
print("You are " + str(userYears) + " years, " + str(userMonths) + " months, and " + str(userDays) + " days old. ")

