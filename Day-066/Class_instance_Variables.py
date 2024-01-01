class Employee:
     company_Name = "Apple"
     No_of_employee = 0

     def __init__(self,name):
          self.name = name
          self.raise_amount = 0.2
          Employee.No_of_employee += 1

     def showDetails(self):
          print(f"The name of the employee is : {self.name} and the raise amount in {self.No_of_employee} sized {self.company_Name} is {self.raise_amount}")

emp = Employee("Harry")
emp.raise_amount = 0.3
emp.company_Name = "Google"
emp.showDetails()
emp = Employee("Harsh")
emp.showDetails()