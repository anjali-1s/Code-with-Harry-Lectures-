x = 4
print(x)

def hello():
     x = 5
     print(f"The local x is {x}")
     print("Hello Harry")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")