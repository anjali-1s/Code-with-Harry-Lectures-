#conditional statements
# >, <, <=, >=, ==, !=
ApplePrice = 10
Budget = 200
if (Budget - ApplePrice > 50):
     print("yes,you can buy 1 more kg apple to the cart.")
elif (Budget - ApplePrice > 20):
     print("Yes, you can buy.")
else:
     print("No, you can't buy")
print("Yay")


# Write a program to print that whether a given number is positive,Negative,or zero.
num = int(input("Enter the number:"))
if num > 0:
     print("Positive Number")
elif num < 0:
     print("Negative")
else:
     print("Zero")
print("I am happy now")