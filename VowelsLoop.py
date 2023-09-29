# Vowels Loop

# vowels = ["a", "e", "i", "o", "u"]

vowelCount = 0

words = input("Enter a word. ")

for v in words:
    if v == "a":
        vowelCount += 1

    elif v == "e":
        vowelCount += 1

    elif v == "i":
        vowelCount += 1

    elif v == "o":
        vowelCount += 1

    elif v == "u":
        vowelCount += 1

    else:
        vowelCount += 0


if vowelCount == 1:
    print("Your word has " + str(vowelCount) + " vowel.")

else:
    print("Your word has " + str(vowelCount) + " vowels.")




