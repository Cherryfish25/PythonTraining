# Grocery List

name = input("Welcome to Python's Italian Restaurant! What is your name? ")

print("Thank you for coming " + name + ", here is your menu! ")

menu = print("Menu: Chicken Alfredo, Lasagna, Macaroni and cheese, Pizza, Ravioli, Rigatoni, Salad, Spaghetti ")

foods = input("What food from our menu would you like? ")

if foods == "Chicken Alfredo" or foods == "chicken alfredo":
    print("It's our specialty here! ")
    caServings = int(input("How many servings of chicken alfredo would you like to make? "))
    noodles = 2
    alfredo_sauce = 0.5
    chicken = 0.5
    broccoli = 0.25
    print("Here are the ingredients you will need: " + str(noodles * caServings) + " cups of noodles, " + str(alfredo_sauce * caServings) + " cups of alfredo sauce, " + str(chicken * caServings) + " cups of chicken, and " + str(broccoli * caServings) + " cups of broccoli.")

elif foods == "Lasagna" or foods == "lasagna":
    print("You must be a real Italian! ")
    lServings = int(input("How many servings of lasagna would you like to make? "))
    lasagna_noodles = 3
    ground_beef = 0.5
    pasta_sauce = 0.5
    cheese = 0.5
    print("Here are the ingredients you will need: " + str(lasagna_noodles * lServings) + " lasagna noodles, " + str(ground_beef * lServings) + " cups of ground beef, " + str(pasta_sauce * lServings) + " cups of pasta sauce, and " + str(cheese * lServings) + " cups of cheese.")

elif foods == "Macaroni and cheese" or foods == "macaroni and cheese":
    print("Sounds good! ")
    macServings = int(input("How many servings of macaroni and cheese would you like to make? "))
    macaroni_shells = 1.5
    milk = 0.5
    cheese = 0.5
    butter = 0.25
    print("Here are the ingredients you will need: " + str(macaroni_shells * macServings) + " cups of macaroni shells, " + str(milk * macServings) + " cups of milk, " + str(cheese * macServings) + " cups of cheese, and " + str(butter * macServings) + " cups of butter.")


elif foods == "Pizza" or foods == "pizza":
    print("My favorite! ")
    pizzaTypes = input("Would you like cheese pizza or pepperoni pizza? ")
    pServings = int(input("How many servings of " + pizzaTypes + " would you like to make? "))
    dough = 0.5
    tomato_sauce = 0.25
    cheese = 0.25
    pepperoni = 8
    if pizzaTypes.lower() == "pepperoni pizza" or pizzaTypes.lower() == "pepperoni":
        print("Here are the ingredients you will need: " + str(dough * pServings) + " lbs of pizza dough, " + str(tomato_sauce * pServings) + " cups of tomato sauce, " + str(cheese * pServings) + " cups of cheese, and " + str(pepperoni * pServings) + " pepperoni slices.")
    elif pizzaTypes.lower() == "cheese pizza" or pizzaTypes.lower() == "cheese":
        print("Here are the ingredients you will need: " + str(dough * pServings) + " lbs of pizza dough, " + str(tomato_sauce * pServings) + " cups of tomato sauce, and " + str(cheese * pServings) + " cups of cheese.")
    else:
        print("That is not a valid option. ")

elif foods == "Ravioli" or foods == "ravioli":
    print("It's just like momma used to make it back in Italy! ")
    rServings = int(input("How many servings of ravioli would you like to make? "))
    ravioli = 10
    marinara_sauce = 0.5
    cheese = 0.25
    spinach = 0.25
    print("Here are the ingredients you will need: " + str(ravioli * rServings) + " ravioli, " + str(marinara_sauce * rServings) + " cups of marinara sauce, " + str(cheese * rServings) + " cups of cheese, and " + str(spinach * rServings) + " cups of spinach.")

elif foods == "Rigatoni" or foods == "rigatoni":
    print("Nice choice! ")
    riServings = int(input("How many servings of rigatoni would you like to make? "))
    rigatoni = 2
    tomato_puree = 0.5
    ground_beef = 0.5
    cheese = 0.5
    print("Here are the ingredients you will need: " + str(rigatoni * riServings) + " cups of rigatoni, " + str(tomato_puree * riServings) + " cups of tomato puree, " + str(ground_beef * riServings) + " cups of ground beef, and " + str(cheese * riServings) + " cups of cheese.")

elif foods == "Salad" or foods == "salad":
    print("What a healthy option! ")
    saServings = int(input("How many servings of salad would you like to make? "))
    lettuce = 2
    tomatoes = 0.5
    cucumber_slices = 0.5
    croutons = 0.25
    shredded_carrot = 0.25
    dressing = 0.25
    print("Here are the ingredients you will need: " + str(lettuce * saServings) + " cups of lettuce, " + str(tomatoes * saServings) + " cups of tomatoes, " + str(cucumber_slices * saServings) + " cups of cucumber slices, " + str(croutons * saServings) + " cups of croutons, " + str(shredded_carrot * saServings) + " cups of shredded carrot, and " + str(dressing * saServings) + " cups of dressing.")

elif foods == "Spaghetti" or foods == "spaghetti":
    print("Excellent choice! ")
    sServings = int(input("How many servings of spaghetti would you like to make? "))
    noodles = 2
    pastaSauce = 0.5
    meatballs = 3
    print("Here are the ingredients you will need: " + str(noodles * sServings) + " cups of noodles, " + str(pastaSauce * sServings) + " cups of pasta sauce, and " + str(meatballs * sServings) + " meatballs.")

else:
    print("That is not an option on the menu. Restart program to enter a valid option. ")