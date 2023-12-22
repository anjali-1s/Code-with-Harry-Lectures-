def fibbonaci(n):
     if (n == 0 or n == 1):
          return n
     else:
          return (fibbonaci(n-1) + fibbonaci(n-2))

n = int(input("Enter the number of terms:"))

for i in range(n):
     print(fibbonaci(i))