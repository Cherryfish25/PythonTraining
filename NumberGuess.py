# Number Guess

import random

answer = random.randint(1,20)

def Guess1():
    Guess1 = int(input("Guess a number from 1 - 20. You have 3 tries. "))
    if Guess1 == answer:
        print("That is the correct answer!")
    else:
        print("That is not the correct answer. Try again. ")
        Guess2()

def Guess2():
    Guess2 = int(input("Guess another number from 1 - 20: "))
    if Guess2 == answer:
        print("That is the correct answer!")
    else:
        print("That is not the correct answer. Try again. ")
        Guess3()

def Guess3():
    Guess3 = int(input("Guess another number from 1- 20: "))
    if Guess3 == answer:
        print("That is the correct answer!")
    else:
        print("That is not the correct answer. The answer was " + str(answer) + ".")

Guess1()