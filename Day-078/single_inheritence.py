class Animal:
     def __init__(self,name,breed):
          self.name = name
          self.breed = breed

     def make_sound(self):
          print("Sound made by the animal")

class Dog(Animal):
     def __init__(self,name,breec):
          Animal.__init__(self,name,species = "Dog")
          # self.breed = breed

     def make_sound(self):
          print("Bark!")

d = Dog("Dog","Dog")
d.make_sound()