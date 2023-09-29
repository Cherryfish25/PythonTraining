# Mad Libs

pluralNoun1 = input("Enter a plural noun: ")
adjective1 = input("Enter an adjective: ")
verb1 = input("Enter a verb ending in 'ing': ")
lastName = input("Enter a last name: ")
food = input("Enter a type of food (plural): ")
name1 = input("Enter a name: ")
name2 = input("Enter another name: ")
number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
number3 = input("Enter another number: ")
adjective2 = input("Enter an adjective: ")

sentence1 = "Today was the first day of school. My teachers name is Mrs. " + lastName + ". She is very " + adjective1 + "."
sentence2 = "Today, we learned about " + pluralNoun1 + ". We also went " + verb1 + " in gym class."
sentence3 = "At lunchtime, I ate " + food + " and talked with my best friends, " + name1 +" and " + name2 + "."
sentence4 = "In math class, we learned that " + number1 + " + " + number2 + " = " + number3 + "."
sentence5 = "I had a " + adjective2 + " first day of school."

print(" ")
print(" ~ First Day of School ~")
print(" ")
print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)
print(sentence5)