# Write a python program to find first digit of a given number.
# Method 1
def getFirstNumber(n):
   while n >= 10:
       n = n//10
   return n
   

n = int(input("Enter the number:"))
print(getFirstNumber(n))

# Method 2
import math

def getfirstdigit(n):
   d = int(math.log10(n))
   res = n // (10 ** d)
   return res

n = int(input("Enter the number:"))
print(getfirstdigit(n))
