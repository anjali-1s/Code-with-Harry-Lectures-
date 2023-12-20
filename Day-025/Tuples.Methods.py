countries = ('Italy','Spain','Germany','Seria','Austria')
temp = list(countries)
temp.append("Russia")                             # Add item
temp.pop(3)                                       # Remove item
temp[2] = "Finland"                               # Change item
countries = tuple(temp)
print(countries)

# Concatination
state1 = ("Telangana","Andhra Pradesh","Tamil Nadu")
state2 = ("Masoori","Himachal Pradesh","Shimla")
res1 = state1+state2
print(res1)

tuple1 = (1,2,3,4,5,6,2,3,4,2,3,4)
res = tuple1.count(2)
print("count of 2 in the given tuple is:",res)
print(tuple1.index(3))

res1 = tuple1.index(2,6,10)
print(res1)

print(len(tuple1))