class Math:

     # constructor
     def __init__(self,num):
          self.num = num

     def addtoNum(self,n):
          self.num = self.num + n
     
     @staticmethod
     def add(a,b):
          return a+b

m = Math(5)
print(m.num)
m.addtoNum(8)
print(m.num)

# static method do not require any object initialisation.
print(Math.add(1,2))
print(m.add(9,8))