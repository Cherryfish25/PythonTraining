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
    "If I could have any superpower...",
    "If I could meet any historical figure...",
    "If I could have any job in the world...",
    "If I could learn any language instantly...",
    "If I could only listen to one music genre...",
    "If I could own any type of vehicle...",
    "If I could have dinner with any celebrity...",
    "If I could only watch one TV show or movie...",
    "If I could have any dessert right now...",
    "If I could visit any famous landmark...",
    "If I could travel to any planet in our solar system...",
    "If I could only read one book for the rest of my life...",
    "If I could have any famous painting hanging in my home...",
    "If I could attend any major sporting event...",
    "If I could have any famous person's autograph...",
    "If I could have any type of magical creature as a companion...",
    "If I could have any instrument to master...",
    "If I could have any famous chef cook for me...",
]

Loves = [
    ["pizza", "cheeseburger", "spaghetti"],
    ["red panda", "dog", "cat", "flamingo", "ferret"],
    ["california", "hawaii", "italy", "paris", "london", "arizona", "japan"],
    ["pink", "white", "black"],
    ["spring"],
    ["chick fil a", "taco bell", "panera bread", "firehouse subs"],
    ["teleportation", "invisibility"],
    ["Jesus", "Albert Einstein"],
    ["youtuber", "singer"],
    ["spanish", "chinese"],
    ["pop"],
    ["jeep", "tesla", "lamborghini"],
    ["harry styles", "taylor swift"],
    ["yes day", "project mc2", "beauty and the beast", "encanto"],
    ["cheesecake", "brownie"],
    ["hollywood sign", "eiffel tower", "golden gate bridge", "statue of liberty", "colosseum"],
    ["the moon"],
    ["girl stuff", "dork diaries", "love & gelato"],
    ["mona lisa", "the starry night", "the great wave off kanagawa"],
    ["super bowl"],
    ["taylor swift", "harry styles", "olivia rodrigo"],
    ["unicorn"],
    ["guitar", "piano"],
    ["gordon ramsay"]

]

Hates = [
    ["sushi", "fish"],
    ["hyena", "lion", "snake", "spider"],
    ["north korea"],
    ["green", "brown"],
    ["summer", "autumn", "fall", "winter"],
    ["mcdonald's", "arby's"],
    ["immortality", "psychokinesis"],
    ["adolf hitler"],
    ["janitor", "military soldier"],
    ["russian"],
    ["country", "jazz"],
    ["van", "motorcycle"],
    ["drake", "justin bieber", "joe biden"],
    ["transformers", "spy cats"],
    ["oatmeal raisin cookie", "pecan pie"],
    ["space needle"],
    ["sun"],
    [""],
    ["whistler's mother"],
    ["cricket world cup"],
    ["drake", "joe biden"],
    ["dragon"],
    ["trombone"],
    ["mario batali"]

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