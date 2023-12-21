import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

Hour = int(time.strftime('%H'))
Hour = int(input("Enter time :"))
print(Hour)

if (Hour >= 0 and Hour < 12):
     print("Good morning sir!")
elif(Hour >= 12 and Hour < 17):
     print("Good afternoon sir!")
if(Hour >= 17 and Hour< 0):
     print("Good Evening sir!")


