# Discount Generator
import random

originalPrice = input("Enter a price. ")

discount = random.randrange(10, 60, 5)

print("You have a " + str(discount) + "% discount.")

discountAmount = float(originalPrice) * (float(discount) * 0.01)

limitedDiscount = round(discountAmount, 2)

print("You have a discount amount of $" + str(limitedDiscount) + ".")

newPrice = float(originalPrice) - limitedDiscount

newPriceLimited = round(newPrice, 2)

print("The price is " + str(newPriceLimited) + ".")






