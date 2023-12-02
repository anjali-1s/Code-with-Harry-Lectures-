# Write a python program to count digits of a given number.
n = int(input("Enter the number:"))
count = 0
while n > 0:
    n = n//10
    count += 1
print(count)
    




