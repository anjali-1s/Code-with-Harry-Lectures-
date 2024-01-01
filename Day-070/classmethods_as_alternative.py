class Employee:
     def __init__(self,name,salary):
          self.name = name
          self.salary = salary

     # alternative constructor---> it works like a constructor but takes data in different format.
     @classmethod
     def fromstr(cls,string):
          return cls(string.split("-")[0],(int(string.split("-")[1])))

     '''@classmethod
     def fromstr(cls,string):
          salary = string.split(',')
          name = string.split(',')
          return cls(name,int(salary))
     '''
emp = Employee("Anjali",12000)
print(emp.name)
print(emp.salary)

string = "Harry-12000"
emp2 = Employee.fromstr(string)
print(emp2.name)
print(emp2.salary)
emp3 = Employee.fromstr("Nandani-20000")
print(emp3.name,emp3.salary)