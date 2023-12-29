class person:
     name = "Anjali Singh"
     occupation = "Software Developer"
     salary = 10,00000

     def info(self):
          print(f"{self.name} is a {self.occupation}")

Object1 = person()
print(Object1.name)
Object1.info()