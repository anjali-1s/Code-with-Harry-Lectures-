import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

name = input("Enter the name:")
hrs = int(time.strftime('%H'))

if 4 <= hrs < 12:
     print(name,"Good Morning!")
elif 12 <= hrs < 17:
     print(name,"Good Afternoon!")
elif 17 <= hrs < 21:
     print(name,"Good Evening!")
else:
     print(name,"Good Night!")
print("Nice to meet you!")