# factorial program
n = int( input("enter the number:"))
res = 1
for i in range(2,n+1):
    res = res*i
print("Factorial is :",res)
