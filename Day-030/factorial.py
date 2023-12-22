# Write a program to demonastrate recursion through factorial program.

def factorial(num):
     if(num == 0 or num == 1):
          return 1
     else:
          return num*factorial(num-1)

num = int(input("Enter the number to find out factorial:"))
res = factorial(num)
print(res)

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 = 120