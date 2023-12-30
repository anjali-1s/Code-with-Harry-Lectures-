# There is nothing like public , protected and private.
# But we use them in pythin.

# All the variables and methods are public by default.
class Employee:

     # constructor
     def __init__(self):
          self.name = "Anjali"                              # public variable
          self.occ = "Engineer"                             # public variable
          self.__place = "Banglore"                         # private variable
          self._food = "momos"                              # mangled variable

e = Employee()
print(e.name)
print(e.occ)


# private members of the class are accessible only inside the class.
# print(e.__place)                   # cannot be accessed directly
print(e._Employee__place)            # can be accessed directly

# Name mangling is used to protect class-private, superclass-private from being accidentally overwritten by subclasses.
print(e._food)                       # mangled variable access
print(e.__dir__())

