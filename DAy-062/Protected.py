# protected members of the classes are accessible inside the class and also by the subclasses.
class Student:

     # constructor
     def __init__(self):
          self._name = "Harry"
     
     def _funName(self):                                    # protected function
          return "CodeWithHarry"

class Subject(Student):                                     # Inheited class
     pass

s = Student()
s1 = Subject()                                              

# calling by object of Student class
print(s._name)
print(s._funName())

# calling by object of Student class
print(s1._name)
print(s1._funName())