# map function applies a function to each element in a sequence and returns the new sequence in transforming elements.
def cube(x):
     return x*x*x

print(cube(2))

'''l = [1,2,3,4,5]
newl = []
for item in l:
     newl.append(cube(item))

print(newl)'''

# with map function
l = [1,2,3,4,5,6]
newl = list(map(cube,l))
print(newl)

numbers = [1,2,3,5,6]
doubled = map(lambda x : x * 2,numbers)
print(list(doubled))