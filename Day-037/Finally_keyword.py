def func1():
     try:
          l = [2,3,4,5,6,7]
          i = int(input("Enter the index:"))
          print(l[i])

     except:
          print("some error occured!")

     finally:
          print("I am always executed!")

x = func1()
print(x)