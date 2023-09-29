import random

print("Hellooooo! In this game, you will answer the questions, and I will tell you if they are correct.")
print("Let's get started!")

# Define questions and corresponding love/hate lists
questions = [
    "If I could only eat one food...",
    "If I could have any animal as a pet...",
    "If I could go anywhere...",
    "If I could only wear one color...",
    "If I had to get rid of any season...",
    "If I could only eat at one fast food place..."
]

love_answers = [
    ["pizza", "cheeseburger", "spaghetti"],
    ["red panda", "dog", "cat", "flamingo", "ferret"],
    ["california", "hawaii", "italy", "paris", "london", "arizona", "japan"],
    ["pink", "white", "black"],
    ["spring"],
    ["chick fil a", "taco bell", "panera bread", "firehouse subs"]
]

hate_answers = [
    ["sushi", "fish"],
    ["hyena", "lion", "snake", "spider"],
    ["north korea"],
    ["green", "brown"],
    ["summer", "autumn", "fall", "winter"],
    ["mcdonald's", "arby's"]
]

# Select a random question
question_index = random.randint(0, len(questions) - 1)
question = questions[question_index]

print(question)

LoveIt = input("I would love if it was: ")
HateIt = input("I would hate if it was: ")

# Define a function to check if the answers are correct
def correct(question, love_answers, hate_answers):
    love_correct = LoveIt in love_answers
    hate_correct = HateIt in hate_answers
    return love_correct, hate_correct

love_correct, hate_correct = correct(question, love_answers[question_index], hate_answers[question_index])

if love_correct:
    print("Your love answer is correct!")
else:
    print("Your love answer is incorrect!")

if hate_correct:
    print("Your hate answer is correct!")
else:
    print("Your hate answer is incorrect!")
