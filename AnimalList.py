# Animal List

import random

favAnimals = [ ]

while len(favAnimals) < 4:
    animal = input("What is one of your favorite animals? ")
    favAnimals.append(animal)

listLength = len(favAnimals)

favFoods = [ ]

while len(favFoods) < 4:
    food = input("What is one of your favorite foods? ")
    favFoods.append(food)

listLength2 = len(favFoods)

favColors = []

while len(favColors) < 4:
    color = input("What is one of your favorite colors? ")
    favColors.append(color)

listLength3 = len(favColors)

print("A " + favAnimals[random.randrange(0, listLength)] + " likes to eat " + favColors[random.randrange(0, listLength3)] + " " + favFoods[random.randrange(0,listLength2)] + " for breakfast!")

print("A " + favAnimals[random.randrange(0, listLength)] + " likes to eat " + favColors[random.randrange(0, listLength3)] + " " + favFoods[random.randrange(0,listLength2)] + " for lunch!")

print("A " + favAnimals[random.randrange(0, listLength)] + " likes to eat " + favColors[random.randrange(0, listLength3)] + " " + favFoods[random.randrange(0,listLength2)] + " for dinner!")

# food = input("What does a " + favAnimals[random.randrange(0,listLength)] + " like to eat? ")
