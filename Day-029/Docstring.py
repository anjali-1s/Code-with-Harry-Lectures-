# function to print the square of a number
def square(n):
     ''' Takes in a number n,returns the square of n'''
     print(n ** 2)

num = int(input("Enter the number:"))
square(num)
print(square.__doc__)