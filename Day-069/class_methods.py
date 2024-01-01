class Employee:
     company = "Apple"

     def show(self):
          print(f"The name is {self.name} and company is : {self.company}")

     @classmethod                            # classmethods provide classes to the function as an argument and we can change class members directly through it.
     def changeCompany(cls,newcompany):
          cls.company = newcompany

emp = Employee()
emp.name = "Anjali"
emp.show()
emp.changeCompany("Google")
emp.show()
print(Employee.company)