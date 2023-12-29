# construcot is a special method in a class which is used to create and initialise an object of a class.
class person:
     name = "Anjali Singh"
     occ = "Software Developer"

     # calling a default constructor
     def __init__(self):
          print("Hey i am a person")

     # multiple arguments constructor
     def __init__(self,n,o):
          print("You are most welcome")
          self.name = n
          self.occ = o

     def info(self):
          print(f"{self.name} is a {self.occ}")

'''a = person()
a.info()
print(a.name)

a.name = "Divya"
a.occ = "teacher"
a.info()'''

res1 = person("Anjali","Developer")
res2 = person("Divya","HR")
res1.info()
res2.info()
