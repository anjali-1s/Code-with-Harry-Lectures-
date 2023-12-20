# default argument
def average(a=9,b=1):
     print("The average of two numbers is:", (a+b)/2)

a = 5
b = 1
average(a,b)

# keyword argument
# it doesn't maintain order
def printNumber(a = 25,b = 45):
     print(a)
     print(b)

printNumber(b = 45,a = 56)

# required arguments
def printSum(a,b=9):
     print("The sum of the fiven number is:",a+b)

printSum(a=12)

# variable length arguments
def average(*numbers):
     sum = 0
     for i in numbers:
          sum = sum + i
     return sum/len(numbers)

res = average(5,5,8,8)
print(res)