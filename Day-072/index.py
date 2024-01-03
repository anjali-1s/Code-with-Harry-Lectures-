class Employee:
     def __init__(self,name,id):
          self.name = name
          self.id = id

class Programmer(Employee):
     def __init__(self,name,id,lang):
          super().__init__(name,id)
          self.lang = lang

rohan = Employee("Rohan Das","420")
Harry = Programmer("Anjali","360","Python")
print(rohan.name)
print(Harry.name)
print(Harry.lang)
print(rohan.id)
print(Harry.id)
