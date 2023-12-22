s1 = {2,4,6,8}
s2 = {3,6,4,9}

print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Kajakistan","Seoul","Kabul","Helesinki"}
# cities3 = cities.union(cities2)
# print(cities3)

# cities2.update(cities)
# print(cities2)

# cities.intersection_update(cities2)
# print(cities)

# Symmetric difference
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities3 = cities.difference(cities2)
# print(cities3)

print(cities.isdisjoint(cities2))

cities3 = {"Tokyo","Madrid","Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities3.add("Austin")
print(cities3)

cities3.remove("Tokyo")
print(cities3)

cities3.discard("Austin")                            # remove will throw an error but discard will not
print(cities3)

item = cities.pop()
print(cities)
print(item)                                          # pop() will remove any last element from the set but the catch is that we dont know which element will be discarded.But, we can access that element.

# del cities
# print(cities)                                      # del is not a method rather than it is a keyword which is used to delete entire set.

cities3.clear()                                      # clear() will clear all the elements of the set and provide an empty set.
print(cities3)

if "Tokyo" in cities:
     print("Tokyo is present")
else:
     print("Tokyo is not present")