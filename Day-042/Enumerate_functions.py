marks = [12,34,56,78,98,78,1,23,45]

# index = 0

# for mark in marks:
#      print(mark)

#      if index == 4:
#           print("Very Good")

#      index += 1


for index,mark in enumerate(marks,start=1):
     print(index,mark)

     if index == 4:
          print("Very Good")

tuple = ('Anjali','Nandani','Prity')
print(tuple)
print(type(tuple))

for index,value in enumerate(tuple):
     print(value,index)

     if index == 2:
          print("It has been over! ")