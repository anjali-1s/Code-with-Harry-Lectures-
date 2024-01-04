class Animal:
     def __init__(self,name,breed):
          self.name = name
          self.breed = breed

     def make_sound(self):
          print("Animals are barking!")

class Cat(Animal):
     def __init__(self,name,breed):
          self.name = name
          self.breed = breed

     def make_sound(self):
          print("Cats are mewing!")

c = Cat("cat","Junglee")
c.make_sound()