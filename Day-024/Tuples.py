tup = (1,2,3,4,5,6)
print(type(tup),tup)

# indexing of tuples
print(tup[0])
print(tup[1])
print(tup[2])

# Negative indexing
print(tup[-1])

if 3 in tup:
     print("3 is present in tup")
else:
     print("No it is not present")

# Slicing
print(tup[1:3])
print(tup[:4])
print(tup[0:])