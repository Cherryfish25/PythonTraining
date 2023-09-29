# Love It or Hate It

import random

print("Hello! In this game, you will answer the questions and I will tell you if they are correct.")
print("Let's get started!")

Questions = [
    "If I could only eat one food...",
    "If I could have any animal as a pet...",
    "If I could go anywhere...",
    "If I could only wear one color...",
    "If I had to get rid of any season...",
    "If I could only eat at one fast food place...",
]

Loves = [
    ["pizza", "cheeseburger", "spaghetti"],
    ["red panda", "dog", "cat", "flamingo", "ferret"],
    ["california", "hawaii", "italy", "paris", "london", "arizona", "japan"],
    ["pink", "white", "black"],
    ["spring"],
    ["chick fil a", "taco bell", "panera bread", "firehouse subs"]
]

Hates = [
    ["sushi", "fish"],
    ["hyena", "lion", "snake", "spider"],
    ["north korea"],
    ["green", "brown"],
    ["summer", "autumn", "fall", "winter"],
    ["mcdonald's", "arby's"]
]

questionIndex = random.randint(0,len(Questions) -1)

userQuestion = Questions[questionIndex]

print(userQuestion)

LoveIt = input("I would love if it was: ")
HateIt = input("I would hate if it was: ")

def correct():

        love_correct = LoveIt in str(Loves[questionIndex])
        if love_correct:
            print("Your answer for 'Love It' is correct.")
        else:
            print("Your answer for 'Love It' is incorrect.")
        hate_correct = HateIt in str(Hates[questionIndex])
        if hate_correct:
            print("Your answer for 'Hate It' is correct.")
        else:
            print("Your answer for 'Hate It' is incorrect.")

correct()