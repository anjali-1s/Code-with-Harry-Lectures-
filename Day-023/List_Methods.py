l = [10,4,3,57,23,4]
print(l)
l.append(12)
l.sort()
print(l)                         # it will sort the list in ascending order

l.sort(reverse = True)
print(l)                         # it will sort the list in descending order

l.reverse()
print(l)                         # it will reverse the list in reverse order

print(l.index(4))                # it will provide the index of the given element

print(l.count(4))                # it will provide the number of times the given element repeated

'''m = l
m[0] = 0
print(l)'''

# instead of this,
# we can write as:

m = l.copy()
m[0] = 0
print(l)
print(m)

l.insert(2,739)
print(l)

n = [10,20,30]
l.extend(n)
print(l)

# if we don't want to change original list then we use concatination
k = l + n
print(k)
print(l)

