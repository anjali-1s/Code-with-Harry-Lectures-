#Match Case Statements
x = int(input("Enter the number:"))

# x is the variable to match
match x:
     # if x is 0
     case 0:
          print("x is zero")
     
     # if x is 1
     case 1:
          print("X is one")
     
     case _:
          print(x)