# Write a program to demonastrate function.

def calculategmean(a,b):
     mean = (a+b)/(a*b)
     print(mean)

a = 9
b = 8
calculategmean(a,b)


def greaterNumber(a,b):
     if(a > b):
          print(a,"is greater than",b)
     elif(a < b):
          print(b,"is greater than",a)
     else:
          print(a,"is equals to",b)

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
greaterNumber(a,b)