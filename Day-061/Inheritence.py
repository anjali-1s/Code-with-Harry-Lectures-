#Base class
class Employee:

     #constructor
     def __init__(self,name,id):
          self.name = name
          self.id = id

     #utility methods
     def showDetails(self):
          print(f"The name of the employee:{self.id} is {self.name}")


#inherited class
class Programmer(Employee):
     def showLanguage(self):
          print("The default language is Python.")


#object creation
e = Employee("Anjali",430)
e.showDetails()
e1 = Programmer("Abhiraj",230)
e1.showDetails()
e1.showLanguage()