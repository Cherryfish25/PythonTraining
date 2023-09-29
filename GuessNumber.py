# Guess Number
import random

Guess = input("Guess a number. (1 - 20) ")

Answer = (random.randint(1,20))

if Guess == Answer:
    print("You guessed the correct number! ")

if Guess != Answer:
    second = input("You guessed incorrectly. Try again. ")

if second == Answer:
    print("You guessed correctly on your second try! ")

if second != Answer:
    third = input("You guessed incorrectly. Guess another number. ")

if third == Answer:
    print("You guessed correctly on your third try! ")

if third != Answer:
    print("You guessed incorrectly. The number was " + str(Answer) + ".")